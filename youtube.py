from pytube import *
link=input("Enter link")

yt=YouTube(link)
videos=yt.streams.all()
print(videos)