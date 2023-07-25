from pytube import YouTube
link = "https://www.youtube.com/watch?v=MIX38vTE_wE  "
youtube_1 = YouTube(link)

print(youtube_1.title)
yt = YouTube("https://www.youtube.com/watch?v=MIX38vTE_wE ")
print(youtube_1.captions)
print(youtube_1.thumbnail_url)
videos = youtube_1.streams.all()
videos = youtube_1.streams.filter(only_audio= True)
vid = list(enumerate(videos))
for i in vid:
    print(i)
print()
strm = int(input("enter : "))
videos[strm].download()
print("successfully")
