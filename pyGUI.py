from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox

'''
SummarizerInterface class creates an interactive user interface that takes in an article from a
user and verifies its length before passing it onto the system.
'''
class SummarizerInterface(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()


    ## Defines and implements all the widgets used in the interface.
    def createWidgets(self):
        self.textBox = scrolledtext.ScrolledText(self,width=40,height=10,
                                                 padx=5,pady=5)
        self.textBox.grid(column=0,row=0,padx=10,pady=10)
        self.textBox.insert(INSERT,'Paste an article here...')

        self.submitButton = Button(self,text='Summarize Article',
                                   command=self.manageInput)
        self.submitButton.grid()

        self.quitButton = Button(self,text='Quit',command=self.quit)
        self.quitButton.grid(pady=20)


    ## Performs a check to see if the user is ready to quit after hitting the 'quit' button.
    def quit(self):
        quitCheck = messagebox.askokcancel(title='Verify Quit',
                                     message="Are you sure you'd like to exit?")
        if quitCheck: Frame.quit(self)


    ## Retrieves the text from the scrolled text box and passes the text to the system
    ## after verifying length.
    def manageInput(self):
        userInput = self.textBox.get('1.0', END)

        if self.verifyLength(userInput) == True:
            print("-" * 22)
            print("Summarizing article...")
            print("-" * 22)
        else:
            print("\nPlease choose an article that is 150 words or less.\n")


    ## Returns true if a string contains 150 words or less.
    def verifyLength(self, text):
        textString = text.split()

        if len(textString) > 150:
            return False
        return True

GUI = SummarizerInterface()
GUI.master.title("Text Summarization Tool")
GUI.mainloop()
