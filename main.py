import customtkinter as ctk
from pytube import YouTube
from threading import Thread

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class YouTubeDownloaderApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title('Youtube Downloader')
        self.geometry('720x480')

        self.url_label = ctk.CTkLabel(self, text="YouTube Video URL:")
        self.url_label.pack(pady=(20, 5))
        
        self.url_entry = ctk.CTkEntry(self, width=400, placeholder_text="Enter YouTube video link here")
        self.url_entry.pack()

        self.download_button = ctk.CTkButton(self, text="Download", command=self.start_download)
        self.download_button.pack(pady=20)

        self.status_label = ctk.CTkLabel(self, text="")
        self.status_label.pack()

    def download_video(self, url):
        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            stream.download()
            self.update_status(f"'{yt.title}' downloaded successfully!")
        except Exception as e:
            self.update_status(f"Error: {e}")

    def start_download(self):
        url = self.url_entry.get()
        if url.strip():
            self.update_status("Downloading...")
            Thread(target=self.download_video, args=(url,)).start()
        else:
            self.update_status("Please enter a YouTube video URL.")

    def update_status(self, text):
        self.status_label.configure(text=text)

if __name__ == '__main__':
    app = YouTubeDownloaderApp()
    app.mainloop()
