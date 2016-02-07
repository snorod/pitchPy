import winsound
note = input("What letter note would you like?: ").upper()
def note2key(note):
    flat = input("Is it flat?: ")
    if (flat.lower() == "yes" or flat.lower() == "y") and (note == "D" or note == "E" or note == "G" or note == "A" or note == "B"):
        note = note + "b"
    else:
        sharp = input("Is it sharp?: ")
        if (sharp.lower() == "yes" or sharp.lower() == "y") and (note == "C" or note == "D" or note == "F" or note == "G" or note == "A"):
            note = note + "s"
    octave = int(input("Which octave?: "))
    noteDict = dict(
    C = 4,
    Cs = 5,
    Db = 5,
    D = 6,
    Ds = 7,
    Eb = 7,
    E = 8,
    F = 9,
    Fs = 10,
    Gb = 10,
    G = 11,
    Gs = 12,
    Ab = 12,
    A = 13,
    As = 14,
    Bb = 14,
    B = 15,
    )
    keyNum = noteDict[note] + 12 * (int(octave) - 1)
    return keyNum
def key2freq(keyNum):
    A4freq = 440
    newFreq = A4freq*(2**((keyNum - 49)/12))
    print("The frequency of this note is " + str(newFreq))
    return newFreq
sound = int(key2freq(note2key(note)))
dur = int(input("How many seconds should it play for?: "))*1000
winsound.Beep(sound,dur)
