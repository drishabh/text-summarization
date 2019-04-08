from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.textBox = scrolledtext.ScrolledText(self,width=40,height=10,
                                                 padx=5,pady=5)
        self.textBox.grid(column=0,row=0,padx=10,pady=10)
        self.textBox.insert(INSERT,'Paste an article here...')

        self.submitButton = Button(self,text='Summarize Article',
                                   command=self.printInput)
        self.submitButton.grid()

        self.quitButton = Button(self,text='Quit',command=self.quit)
        self.quitButton.grid(pady=20)

    def quit(self):
        quitCheck = messagebox.askokcancel(title='Verify Quit',
                                     message="Are you sure you'd like to exit?")
        if quitCheck: Frame.quit(self)

    def printInput(self):
        userInput = self.textBox.get('1.0', END)
        print(userInput)

app = Application()
app.master.title("Text Summarization Tool")
app.mainloop()
