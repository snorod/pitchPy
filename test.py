from Tkinter import *
root = Tk() #Makes the window
root.wm_title("pitchPy") #Makes the title that will appear in the top left
root.config(background = "#FFFFFF") #sets background color to white

#put widgets here
def btnClicked:
    return true

leftFrame = Frame(root, width=200, height = 600)
leftFrame.grid(row=0, column=0, padx=10, pady=2)

firstLabel = Label(leftFrame, text="This is my first label")
firstLabel.grid(row=0, column=0, padx=10, pady=2)

userInput = Entry(leftFrame, width = 10) #the width refers to the number of characters
userInput.grid(row=1, column=0, padx=40, pady=2)
#get the text inside of userInput
lol = userInput.get()
print(lol)

newButton = Button(leftFrame, text="C", command=btnClicked)
newButton.grid(row=0, column=0, padx=10, pady=2)

root.mainloop() #start monitoring and updating the GUI. Nothing below here runs.
