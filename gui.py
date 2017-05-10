from Tkinter import *
import Tkinter as tk
import tweepy
from secrets import *
import Tkinter, Tkconstants, tkFileDialog
from tkMessageBox import *
from PIL import Image, ImageTk
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

class TwitterGUI(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        master.minsize(width=300, height=65) #main frame size
        master.resizable(width=False, height=False)
        self.configure(background="#52a7e9")#main frame bg color
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        self.instructions = Label(self, bg="#52a7e9", text="Enter your tweet")
        self.instructions.grid(row = 0, column = 2, columnspan = 2, sticky = W)
        
        # tweet entry widget
        self.tweet = Entry(self)
        self.tweet.grid(row=0, column = 4,  sticky=W,columnspan=3)
        
        self.photo = ImageTk.PhotoImage(file="twitter.png")
        self.twitter_icon = Label(self, image=self.photo, borderwidth=0)
        self.photo.image = self.photo
        self.twitter_icon.grid(row = 0, column = 0, sticky = W, rowspan=2)
        
        self.tweet_button = Button(self, text="Submit", command = self.post_tweet)
        self.tweet_button.grid(row = 0, column = 5, padx=3, pady=3, sticky=W)
        
        self.instructions = Label(self, bg="#52a7e9",text="Post Picture")
        self.instructions.grid(row = 1, column = 2, columnspan = 2, sticky = W)
        
        self.picture_text = Entry(self)
        self.picture_text.grid(row=1, column = 4)
        
        self.open_file = Button(self, text="Browse", command = self.post_picture)
        self.open_file.grid(row = 1, column = 5,padx=3,pady=3, sticky=E)
        
        menubar = Menu(root)
        
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        helpmenu = Menu(menubar, tearoff=0)
        # add help menu items here
        helpmenu.add_cascade(label="How to Use this App", command=self.how_to)
        helpmenu.add_cascade(label="About", command=self.about_menu)
        
        menubar.add_cascade(label="Help", menu = helpmenu)
        
        root.config(menu=menubar)
        
        
    def post_tweet(self):
        content = self.tweet.get()
        if not content:
            showerror("Warning","You must input text to tweet.")
        if len(content) > 160:
            showinfo("Error", "Too many characters: ", len(content))
        else:
            api.update_status(content)
            showinfo("Success","Tweet successful")

             

    def post_picture(self):
        global picture_text
        picture_name = tkFileDialog.askopenfilename(filetypes = (("jpeg", "*.jpg"), ("bmp", "*.bmp"), ("png", "*.png"),("All files", "*.*")))
        content = self.tweet.get()
        if not picture_name:
            return
        if content:
            api.update_with_media(picture_name, content)
#            picture_text.delete(0, END)
#            picture_text.insert(0, self.picture_name)
            showinfo("Success","Tweet successful")
            
        
        else: 
#            picture_text.delete(0, END)
#            picture_text.insert(0, self.picture_name)
            api.update_with_media(picture_name)
            
            showinfo("Success","Tweet successful")
            
      
        
#    def entry_text(self):
#        text = self.str(picture_name).get()
#        picture_text.delete(0, END)
#        picture_text.insert(0,text)
#        return
        
    def about_menu(self):
        showinfo("About","This was created by me, Gabe.\nIt is my first ever, usable Python \nproject.  I hope you enjoy.")
        
    def how_to(self):
        showinfo("How To", "How to goes here.")
    

root = Tk()
#root.resizable(width=False, height=False)
my_twitter = TwitterGUI(root)
root.title("Twitter GUI")
root.iconbitmap("twitter_24.ico")
root.mainloop()
