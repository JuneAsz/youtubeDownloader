from pytube import YouTube as youtube
from pytube import Playlist
import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import Label
from tkinter import Text


#function that checks if a certain path exists, if not - makes said path

def checkPath(pathdir):
    if os.path.exists(pathdir):
        return
    else:
        os.mkdirs(pathdir)


# downloading video, takes youtube url and directory path as parameters

def downloadVideo(videoLink, path):
    yt = youtube(videoLink)
    print(f"Downloading: {yt.title}")
    checkPath(path)
    yt.streams.filter(only_audio=True).last().download()
    print(f"{yt.title} has finished downloading!")



#downloading playlist, takes youtube url and directory path as parameters


def downloadPlaylist(playlistLink, path):
    playlist = Playlist(playlistLink)
    playlistUrls = list(playlist.video_urls)
    print(playlistUrls)
    checkPath(path)
    for url in playlistUrls:
        yt = youtube(url)
        print(f"Downloading: {yt.title}")
        yt.streams.filter(only_audio=True).last().download(output_path = path)
        print(f"{yt.title} has finished downloading!")
    print("Playlist has finished downloading!")

# function that opens file explorer and asks user for a directory to use


def browse_button():
    global filename
    filename = filedialog.askdirectory()
    fileDirectory.configure(text=filename)


# download button function, checks if URL is playlist or not, and calls the downloading function associated with the input given
# takes video url from the label


def download_button():
    videoLink = youtubeVideo.get()
    targetPath = filename
    if "playlist?list" in videoLink:
        downloadPlaylist(videoLink, targetPath)
    else:
        downloadVideo(videoLink, targetPath)

#Tkinter things

#Initialize an object of class Tk

root = Tk()

#Add color / Title to application, add resolution


root.configure(background="#86726c")
root.title("ytDownloader")
root.geometry("800x450")

#Download button 

button2 = Button(text="Select download directory", command=browse_button)
button2.place(x=1, y=425)

#No fucking clue.

frm = ttk.Frame(root, padding=10)
frm.place()


#Directory location / button

filename = StringVar()
fileDirectory = Label(root, text = filename)
fileDirectory.place(x = 155, y=430)


#youtube URL location

Label(root, text="Input a link a below:").place(x = 351, y = 1)
youtubeVideo = Entry(root, width=150)
youtubeVideo.place(x=1, y=50)


#Download button

downloadButton = Button(root, width=50, height = 2, text="Download", command=download_button).place(x=225, y = 385)


#Exit button

quitButton = Button(root, width = 15, text="Quit", command=root.destroy).place(x=685, y=425)


root.mainloop()

