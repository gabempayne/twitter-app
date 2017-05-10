from Tkinter import *
import Tkinter as tk
import tweepy
from secrets import *
import Tkinter, Tkconstants, tkFileDialog
from tkMessageBox import *

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

class TwitterGUI(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        master.minsize(width=300, height=75) #main frame size
        #master.resizable(width=False, height=False)
        self.configure(background="#00aced")#main frame bg color
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        self.instructions = Label(self, bg="#00aced", text="Enter your tweet")
        self.instructions.grid(row = 0, column = 2, columnspan = 2, sticky = W)
        
        self.tweet = Entry(self)
        self.tweet.grid(row=0, column = 4, sticky = W)
        
        self.photo = PhotoImage(file="twitter.gif") 
        self.twitter_icon = Label(self, image=self.photo, borderwidth=0)
        self.photo.image = self.photo
        self.twitter_icon.grid(row = 0, column = 0, sticky = W)
        
        self.tweet_button = Button(self, text="Tweet", command = self.post_tweet)
        self.tweet_button.grid(row = 0, column = 5, padx=1,sticky=W)
        
        self.instructions = Label(self, bg="#00aced",text="Post Picture")
        self.instructions.grid(row = 1, column = 2, columnspan = 2, sticky = W)
        
        self.picture_text = Entry(self)
        self.picture_text.grid(row=1, column = 4, sticky = W)
        
        self.open_file = Button(self, text="Open", command = self.post_picture)
        self.open_file.grid(row = 1, column = 5,padx=1, sticky=W)
        
        menubar = Menu(root)
        
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_cascade(label="Help", command=self.help)
        
        root.config(menu=menubar)
           
    def post_tweet(self):
        content = self.tweet.get()
        try:
            api.update_status(content)
            showinfo("Success","Tweet successful")
            
        except:
             showerror("Warning","You must input text to tweet.")

        
    def post_picture(self):
        picture_name = tkFileDialog.askopenfilename(filetypes = (("jpeg", "*.jpg"), ("bmp", "*.bmp"), ("png", "*.png"),("All files", "*.*")))
        
        api.update_with_media(picture_name, "I'm sorry about the random spam stuff.. I'm developing something.")
        
    # TODO - add picture/text entry
    def entry_text(self):
        picture_text.delete(0, END)
        picture_text.insert(0,self)
        return
    # TODO - make full help menu
    def help(self):
        showinfo("About","I made a thing!")
    

root = Tk()
#root.resizable(width=False, height=False)
twitter_gui = TwitterGUI(root)
root.title("Twitter Gui")
root.mainloop()