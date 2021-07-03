from tkinter import *
from typing import TypedDict
from pytube import YouTube
import urllib



def download():
    link = link_input.get()
    print(link)
    print(type(link))


    yt = YouTube(link)

    image_url = yt.thumbnail_url
    print(image_url)
    urllib.urlretrieve(image_url,"image.jpg")

root = Tk()
root.geometry("320x200")
root.maxsize(600,200)
root.minsize(600,200)

link_name = Label(root,text="Link ")
link_name.grid(column=1,row=0)
link_input = Entry(root)
link_input.grid(column=2,row=0)

bt = Button(root,text="Download",command=download)
bt.grid(row=1,column=1)
root.mainloop()