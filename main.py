import tkinter
import customtkinter
from pytube import YouTube

def download_video(url, path='.', quality='highest'):
    """
    Download a video from YouTube.

    Parameters:
        url (str): The URL of the YouTube video.
        path (str, optional): The path where the video will be saved. Defaults to the current directory.
        quality (str, optional): The quality of the video ('highest', 'lowest', or a resolution like '720p'). Defaults to 'highest'.
    """
    try:
        # Create a YouTube object with the URL
        yt = YouTube(url)

        # Get the video stream
        if quality == 'highest':
            stream = yt.streams.get_highest_resolution()
        elif quality == 'lowest':
            stream = yt.streams.get_lowest_resolution()
        else:
            stream = yt.streams.filter(res=quality, file_extension='mp4').first()

        if stream:
            # Download the video
            print(f"Downloading '{yt.title}'...")
            stream.download(output_path=path)
            print("Download completed!")
        else:
            print("Could not find a video stream with the specified quality.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    video_url = input("Enter the YouTube video URL: ")
    download_path = input("Enter download path (leave blank for current directory): ") or '.'
    video_quality = input("Enter video quality ('highest', 'lowest', or a resolution like '720p'): ") or 'highest'

    download_video(video_url, download_path, video_quality)
