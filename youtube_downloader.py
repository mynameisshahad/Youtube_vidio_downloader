
from pytube import YouTube

link = input("Enter YouTube video URL: ")
yt = YouTube(link)

print(f"Title: {yt.title}")
print("1. Download Video")
print("2. Download Audio Only")

choice = input("Enter your choice (1/2): ")

if choice == "1":
    stream = yt.streams.get_highest_resolution()
    stream.download()
    print("Video downloaded successfully!")
elif choice == "2":
    stream = yt.streams.filter(only_audio=True).first()
    stream.download(filename=f"{yt.title}.mp3")
    print("Audio downloaded successfully!")
else:
    print("Invalid choice.")
