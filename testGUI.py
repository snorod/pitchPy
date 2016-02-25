from Tkinter import *
import winsound
import sys
import pyaudio
import wave
from matplotlib.mlab import find
import numpy as np
import math
from PIL import Image # wtf

def playSound():
    note = userInput.get()
    note = note.upper()
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
        A4freq = 440
        targetFreq = A4freq*(2**((keyNum - 49.0)/12))
        winsound.Beep(int(round(targetFreq)),5000)
    #else:
    #    print("That's not a real note you goon lmao")
    userInput.delete(0, END)

def stopNote():
    shouldRecord = False
    noteCanvas.create_text(50, 50, width=0, text='C#', font=('Times New Roman',36))

def recordNote():
    noteCanvas.delete(ALL)

#############################################################################################
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 5
    #RECORD_SECONDS = stopNote()
    #WAVE_OUTPUT_FILENAME = "newAudio.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    frames = []
    freqs = []
    #freqDiffs = []
    #freqLowDiffs = []
    #freqLowerDiffs = []
    #freqHighDiffs = []
    #freqHigherDiffs = []
    shouldRecord = True

    #def findDiff(freq, targetFreq):
    #    return abs((freq-targetFreq) * 100.0 /targetFreq)

    #for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    while shouldRecord:
        signal = stream.read(CHUNK)
        frames.append(signal)
        #sec = RECORD_SECONDS - float(CHUNK)/RATE*i
        signal = np.fromstring(signal, 'Int16');
        crossing = [math.copysign(1.0, s) for s in signal]
        index = find(np.diff(crossing));
        f0=round(len(index) *RATE /(2*np.prod(len(signal))))
        freq = f0*2
        freqs.append(freq)
        #freqLow = freq / 2
        #freqLower = freqLow / 2
        #freqHigh = freq * 2
        #freqHigher = freqHigh * 2
        # print("%f Frequency" %freq)
        #freqDiffs.append(findDiff(freq, targetFreq))
        #freqLowDiffs.append(findDiff(freqLow, targetFreq))
        #freqLowerDiffs.append(findDiff(freqLower, targetFreq))
        #freqHighDiffs.append(findDiff(freqHigh, targetFreq))
        #freqHigherDiffs.append(findDiff(freqHigher, targetFreq))
        #if (sec - int(sec)) < 0.01:
        #    print(int(sec))

    #print("Done!\n")
    # print(freqDiffs)
    #def findAcc(diffs):
    #    return round(100 - np.median(diffs))
    #bestAcc = max(findAcc(freqDiffs),findAcc(freqLowDiffs),findAcc(freqLowerDiffs),findAcc(freqHighDiffs),findAcc(freqHigherDiffs))
    # np.mean()

    #acc = str(bestAcc)
    # 100 - bestAcc
    #if bestAcc >= 95:
    #    print("On pitch; " + acc + '%'' accurate!')
    #else:
    #    print("Not on pitch :/\n")
#MINIMUM OF MODULO OF LOWEST FREQUENCY FOR EACH NOTE WILL GIVE WHICH NOTE IT LIKELY IS
#PUT IN COUNTER
    stream.stop_stream()
    stream.close()
    p.terminate()

    #wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    #wf.setnchannels(CHANNELS)
    #wf.setsampwidth(p.get_sample_size(FORMAT))
    #wf.setframerate(RATE)
    #wf.writeframes(b''.join(frames))
    #wf.close()

########################################################################################

root = Tk() #Makes the window
root.wm_title("pitchPy") #Makes the title that will appear in the top left
#root.config(background = "#FFFFFF")
root.config(background = 'white')

#topFrame = Frame(root, width = 100, height = 100)
#topFrame.grid(row=0,column=0,padx=10,pady=2)

#Left Frame and its contents
leftFrame = Frame(root, width=100, height = 100)
leftFrame.grid(row=0, column=0, padx=10, pady=2)

Label(leftFrame, text="Play a note:").grid(row=1, column=0, padx=10, pady=2)
#Instruct = Label(leftFrame, text="Please enter a note")
#Instruct.grid(row=1, column=0, padx=10, pady=2)
userInput = Entry(leftFrame, width = 10) #the width refers to the number of characters
userInput.grid(row=2, column=0, padx=40, pady=2)
#play = Button(leftFrame, text="Play", command = userInput.get())
play = Button(leftFrame, text="Play", command = playSound)
play.grid(row=3, column=0, padx=10, pady=2)

try:
    photo = PhotoImage(file = 'pycharm_logo2.gif')
    Label(leftFrame, image=photo).grid(row=0, column=0, padx=10, pady=2)
except:
    print("Image not found")

#Right Frame and its contents
rightFrame = Frame(root, width=200, height = 800)
rightFrame.grid(row=0, column=1, padx=10, pady=2)
Label(rightFrame, text="Pitch practice:").grid(row=0, column=0, padx=10, pady=2)

noteCanvas = Canvas(rightFrame, width=100, height=100, bg='white')
noteCanvas.grid(row=1, column=0, padx=10, pady=2)

btnFrame = Frame(rightFrame, width=200, height = 200)
btnFrame.grid(row=2, column=0, padx=10, pady=2)

#colorLog = Text(rightFrame, width = 30, height = 10, takefocus=0)
#colorLog.grid(row=3, column=0, padx=10, pady=2)

recBtn = Button(btnFrame, text="Record", command=recordNote)
recBtn.grid(row=0, column=0, padx=10, pady=2)

stopBtn = Button(btnFrame, text="Stop", command=stopNote)
stopBtn.grid(row=0, column=1, padx=10, pady=2)

root.mainloop() #start monitoring and updating the GUI
