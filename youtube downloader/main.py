import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter.scrolledtext import ScrolledText
from pytube import YouTube
from pytube import Playlist
from datetime import datetime
import time
import os
import threading
from PIL import Image, ImageTk


class YoutubeDownloader:
    def setup_root(self):
        self.root = tk.Tk()
        self.root.geometry('700x600')
        self.root.title("Youtube Downloader")
        self.root['bg'] = 'white'


    def setup_Frames(self):
        self.single_vid_frame = tk.Frame(self.root, width=350, height=600, bd=2, bg='white')
        self.playlist_frame = tk.Frame(self.root, width=350, height=600, bd=2, bg='white')
        self.single_vid_frame.grid(row=0, column=0, padx=10, pady=10)
        self.playlist_frame.grid(row=0, column=1, padx=10, pady=10)
        self.setup_btns_and_inputs()

    def downloading_status(self, bytes_remaining, *args):
        print("pava")
        if bytes_remaining < 10000:
            self.MessageVariable.set(f"downloaded {self.video.title}")

    def dowload_video(self):
        print("a1")
        self.video_url = self.url_Entry.get()
        if self.video_url is None:
            messagebox.showwarning("Error", "Enter youtube video link")
        elif "https://" not in self.video_url:
            messagebox.showerror("Error", "Incorrect youtube video")
        else:
            try:
                self.video = YouTube(self.video_url, on_progress_callback=self.downloading_status)
                self.stream = self.video.streams.filter(only_audio=False).first()
            except Exception as e:
                print(e)
                messagebox.showerror("NetworkError", "No Internet Connection")
                return 
            try:
                self.path = filedialog.askdirectory()
                self.MessageVariable = tk.StringVar()
                self.MessageVariable.set(f"Downloading video {self.video.title}")
                self.dowloading_video_label = tk.Label(self.single_vid_frame, textvariable=self.MessageVariable, padx=10, pady=10)
                self.stream.download(output_path = self.path ,filename=None)
                self.dowloading_video_label.pack()
                
            except Exception as e:
                print(e)
                messagebox.showerror("Error", "something went Wrong")


    def setup_btns_and_inputs(self):
        self.download_video_label = tk.Label(self.single_vid_frame, text="Download Video", padx=10, pady=10, bg="white")
        self.playlist_dowload_label = tk.Label(self.playlist_frame, text="Download Playlist", padx=10, pady=10, bg="white")

        self.playlist_url = tk.Entry(self.playlist_frame, width=35, bd=3)
        self.url_Entry = tk.Entry(self.single_vid_frame, width=35,bd=3)

        self.playlist_dowload_btn = tk.Button(self.playlist_frame, text='Download', padx=10, pady=10, command=self.dowload_video)
        self.video_download_btn = tk.Button(self.single_vid_frame, text='Download', padx=10, pady=10)



        self.download_video_label.pack()
        self.playlist_dowload_label.pack()

        self.playlist_url.pack()
        self.url_Entry.pack()

        self.video_download_btn.pack()
        self.playlist_dowload_btn.pack()
    def __init__(self):
        self.setup_root()
        self.setup_Frames()
        self.root.mainloop()


if __name__ == '__main__':
    YoutubeDownloader()