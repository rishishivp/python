import tkinter as tk
from pytube import YouTube
from tkinter import messagebox
from tkinter import filedialog

def downloadvideo():
    url=urlentry.get()
    try:
        yt=YouTube(url)
        stream=yt.streams.get_highest_resolution()
        destinationfolder=filedialog.askdirectory()
        messagebox.showinfo("Your video is downloading ", f"downloading{yt.title}")
        stream.download(destinationfolder)
        messagebox.showinfo("Sucsessfully downloaded.")
    except Exception as e:
        messagebox.showerror("ERROR")
    
root=tk.Tk()
root.title("Youtube Downloader")
root.configure(bg="cyan")
urllabel=tk.Label(root,text="Youtube URL")
urllabel.pack()
urlentry=tk.Entry(root,width=50)
urlentry.pack()
downloadbutton=tk.Button(root,text="download",command=downloadvideo)
downloadbutton.pack()
root.mainloop()
