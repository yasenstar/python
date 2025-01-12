from pytube import YouTube

video_url = input("Please paste YouTube video URL: ")

yt = YouTube(video_url)

stream = yt.streams.get_highest_resolution()

stream.download()