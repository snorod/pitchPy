import winsound
import sys
note = input("Note: ").upper()
def note2key(note):
    if note.find("#") > -1:
        note = note[0] + "S"
    elif note.find("B") > -1:
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
    newFreq = A4freq*(2**((keyNum - 49)/12))
    print("The frequency of this note is " + str(newFreq))
    return newFreq
if note2key(note) > 0:
    sound = int(key2freq(note2key(note)))
    winsound.Beep(sound,5000)
else:
    print("That's not a real note you goon lmao")
    sys.exit()
