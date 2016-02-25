# Stephen Norod, Georgia Tech '19
# some code sampled from PyAudio Documentation and ederwander
# currently working on a GUI that shows you what note you played instead of simply comparing to another note

import winsound
import sys
note = raw_input("Note: ")
note = note.upper()
def note2key(note):
    if note.find("#") > -1:
        note = note[0] + "S"
    elif note.find("B") > 0:
        note = note[0] + "B"
    noteDict = dict(
    C = 40,
    CS = 41,
    DB = 41,
    D = 42,
    DS = 43,
    EB = 43,
    E = 44,
    F = 45,
    FS = 46,
    GB = 46,
    G = 47,
    GS = 48,
    AB = 48,
    A = 49,
    AS = 50,
    BB = 50,
    B = 51,
    )
    if note in noteDict:
        keyNum = noteDict[note]
        return keyNum
    else:
        return 0
def key2freq(keyNum):
    A4freq = 440
    newFreq = A4freq*(2**((keyNum - 49.0)/12))
    print("The frequency of this note is " + str(newFreq))
    return newFreq
if note2key(note) > 0:
    targetFreq = key2freq(note2key(note))
    winsound.Beep(int(round(targetFreq)),5000)
else:
    print("That's not a real note you goon lmao")
    sys.exit()

import pyaudio
import wave

from matplotlib.mlab import find
import numpy as np
import math

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "newAudio.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

raw_input("Match the pitch! (Press Enter to start) ")

def freqCalc(signal):
    signal = np.fromstring(signal, 'Int16');
    crossing = [math.copysign(1.0, s) for s in signal]
    index = find(np.diff(crossing));
    f0=round(len(index) *RATE /(2*np.prod(len(signal))))
    return f0;

frames = []
freqDiffs = []
freqLowDiffs = []
freqLowerDiffs = []
freqHighDiffs = []
freqHigherDiffs = []

def findDiff(freq, targetFreq):
    return abs((freq-targetFreq) * 100.0 /targetFreq)

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
    sec = RECORD_SECONDS - float(CHUNK)/RATE*i
    freq = freqCalc(data)*2
    freqLow = freq / 2
    freqLower = freqLow / 2
    freqHigh = freq * 2
    freqHigher = freqHigh * 2
    # print("%f Frequency" %freq)
    freqDiffs.append(findDiff(freq, targetFreq))
    freqLowDiffs.append(findDiff(freqLow, targetFreq))
    freqLowerDiffs.append(findDiff(freqLower, targetFreq))
    freqHighDiffs.append(findDiff(freqHigh, targetFreq))
    freqHigherDiffs.append(findDiff(freqHigher, targetFreq))
    if (sec - int(sec)) < 0.01:
        print(int(sec))

print("Done!\n")
# print(freqDiffs)
def findAcc(diffs):
    return round(100 - np.median(diffs))
bestAcc = max(findAcc(freqDiffs),findAcc(freqLowDiffs),findAcc(freqLowerDiffs),findAcc(freqHighDiffs),findAcc(freqHigherDiffs))
# np.mean()

acc = str(bestAcc)
# 100 - bestAcc
if bestAcc >= 95:
    print("On pitch; " + acc + '%'' accurate!')
else:
    print("Not on pitch :/\n")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
