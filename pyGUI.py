from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from newspaper import *
import nltk

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
        self.lbl = Label(self,text="Enter an article URL below:")
        self.lbl.grid(column=0,row=0)
        
        self.url = Entry(self,width=40)
        self.url.grid(column=0,row=1)

        self.urlSubmit = Button(self,text='Submit URL',command=self.manageURL)
        self.urlSubmit.grid(column=0,row=2,pady=10)
        
        self.textBox = scrolledtext.ScrolledText(self,width=40,height=10,padx=5,pady=5)
        self.textBox.grid(column=0,row=3,padx=10,pady=10)
        self.textBox.insert(INSERT,'Paste an article here...')

        self.submitButton = Button(self,text='Summarize Article',command=self.manageInput)
        self.submitButton.grid(column=0,row=4)

        self.quitButton = Button(self,text='Quit',command=self.quit)
        self.quitButton.grid(column=0,row=5,pady=20)


    ## Performs a check to see if the user is ready to quit after hitting the 'quit' button.
    def quit(self):
        quitCheck = messagebox.askokcancel(title='Verify Quit',
                                     message="Are you sure you'd like to exit?")
        if quitCheck: Frame.quit(self)


    ## Retrieves the text from the scrolled text box and passes the text to the system
    ## after verifying length.
    def manageInput(self):
        userInput = self.textBox.get('1.0', END)

        if self.verifyLength(150, userInput) == True:
            print("-" * 22)
            print("Summarizing article...")
            print("-" * 22)

            file = open("article.txt", "w")
            file.write(userInput)
            file.close()

    ## Passes content from URL textbox to articleContent function
    def manageURL(self):
        userURL = self.url.get()
        articleTitle,articleText = self.articleContent(userURL)

        self.textBox.delete('1.0', END)
        self.textBox.insert(INSERT, articleText)

    ## Returns true if a string contains 150 words or less.
    def verifyLength(self, length, text):
        textString = text.split()
        num = int(length)

        if len(textString) > num:
            lengthWarning = messagebox.askokcancel(title="Article too long!",
                                                   message="Please provide an article that is 150 words or less.")
            self.textBox.delete('1.0', END)
            return False
        return True

    ## Returns article content from a URL
    def articleContent(self, url):
        newsArticle = Article(url, language="en")
        newsArticle.download()
        newsArticle.parse()
        newsArticle.nlp()
        return(newsArticle.title, newsArticle.text)


GUI = SummarizerInterface()
GUI.master.title("Text Summarization Tool")
GUI.mainloop()
