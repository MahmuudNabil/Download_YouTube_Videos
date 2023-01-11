from tkinter import * 
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube
from pytube import Playlist
from pytube import Channel
import time
from threading import *
# import threading

root = Tk()
root.title("Dowload youtube Videos")
root.geometry("600x400")
root.resizable(FALSE , FALSE)

# My Functions
def browse():
    directory = filedialog.askdirectory(title= "Save Video")
    folderLink.delete(0, "end")
    folderLink.insert(0 , directory)

def finish(stream =None, chunk=None, file_handle=None, remaining=None):
    status.config(text="Status : Complete")

def down_yt():
    status.config(text="Status : Downloading ...")
    link = ytlink.get()
    folder = folderLink.get()
    try:
        YouTube(link, on_complete_callback=finish).streams.filter(progressive = True , file_extension = "mp4").order_by("resolution").desc().first().download(folder)
    except:
        messagebox.showerror("Error","You Must Put Valid YouTube link")


def down_playlist():
    status.config(text="Status : Downloading ...")
    link = ytlink.get()
    folder = folderLink.get()
    p = Playlist(link)
    try:    
        for video in p.videos:
            video.streams.filter(progressive = True , file_extension = "mp4").order_by("resolution").desc().first().download(folder)
        status.config(text="Status : Complete")
    except:
        messagebox.showerror("Error","You Must put valid playlist Link")


def down_type():
    your_option = mygroup.get()
    if your_option == "video":
        down_yt()
        time.sleep(1)
    elif your_option == "playlist":
        down_playlist()
        time.sleep(1)
    else:
        messagebox.showerror("Error","You Must Choose What do you want to Download?")
        time.sleep(1)

def threading():
    # Call work function
    t1=Thread(target=down_type)
    t1.start()

#YouTube Logo
ytphoto = PhotoImage(file="youtube.png").subsample(2)
ytlogo = Label(root, image=ytphoto)
ytlogo.place(relx=0.5 , rely= 0.25, anchor="center")

# Choose what Want to Download 
ch_label = Label(root, text= "Choose What do you want to download?",font="Calibre 10 bold", fg="black")
ch_label.place(x = 170 , y=170)

mygroup = StringVar()
op_video = ttk.Radiobutton(root, text= 'Video'    ,variable=mygroup, value="video").place(x= 230 , y=190)
op_plist = ttk.Radiobutton(root, text= 'PlayList' ,variable=mygroup, value="playlist").place(x= 230 , y=210)


# YouTube Video Link
ytlabel = Label(root , text="YouTube Link")
ytlabel.place(x=25 , y= 245)

ytlink = Entry(root , width= 60)
ytlink.place(x= 140 , y= 245)

# Download Folder
folderLabel = Label(root, text= "Download Folder")
folderLabel.place(x= 25 , y= 278)

folderLink = Entry(root , width=50)
folderLink.place(x=140 , y=278)

#Browse Button
btn_browse = Button(root , text="Browse" , command= browse)
btn_browse.place(x=455 , y=275) 

#Download Button
# btn_download =  Button(root, text="Download" , command= threading.Thread(target= down_type).start)
btn_download =  Button(root, text="Download" , command=threading)
btn_download.place(x=280 , y=315)

# Status Bar
status = Label(root , text="Status : Ready" , font="Calibre 10 italic", fg="black", bg="white" , anchor="w")
status.place(rely= 1, anchor="sw", relwidth=1)



root.mainloop()