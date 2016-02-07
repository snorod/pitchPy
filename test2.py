from Tkinter import *

root = Tk() #Makes the window
root.wm_title("pitchPy") #Makes the title that will appear in the top left
root.config(background = "#FFFFFF")


#Left Frame and its contents
leftFrame = Frame(root, width=200, height = 600)
leftFrame.grid(row=0, column=0, padx=10, pady=2)

Label(leftFrame, text="Instructions:").grid(row=0, column=0, padx=10, pady=2)
Instruct = Label(leftFrame, text="Please enter a note")
Instruct.grid(row=1, column=0, padx=10, pady=2)
userInput = Entry(leftFrame, width = 10) #the width refers to the number of characters
userInput.grid(row=2, column=0, padx=40, pady=2)
play = Button(leftFrame, text="Play", command = userInput.get())
play.grid(row=3, column=0, padx=10, pady=2)


def redCircle():
    circleCanvas.create_text(50, 50, width=0, text=play)
    colorLog.insert(0.0, play + "\n")

try:
    imageEx = PhotoImage(file = 'image.gif')
    Label(leftFrame, image=imageEx).grid(row=2, column=0, padx=10, pady=2)
except:
    print("Image not found")

#Right Frame and its contents
rightFrame = Frame(root, width=200, height = 600)
rightFrame.grid(row=0, column=1, padx=10, pady=2)

circleCanvas = Canvas(rightFrame, width=100, height=100, bg='white')
circleCanvas.grid(row=0, column=0, padx=10, pady=2)

btnFrame = Frame(rightFrame, width=200, height = 200)
btnFrame.grid(row=1, column=0, padx=10, pady=2)

colorLog = Text(rightFrame, width = 30, height = 10, takefocus=0)
colorLog.grid(row=2, column=0, padx=10, pady=2)

redBtn = Button(btnFrame, text="Red", command=redCircle)
redBtn.grid(row=0, column=0, padx=10, pady=2)

yellowBtn = Button(btnFrame, text="Red", command=redCircle)
yellowBtn.grid(row=0, column=1, padx=10, pady=2)



root.mainloop() #start monitoring and updating the GUI
print(note)
