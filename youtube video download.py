from pytube import YouTube
video=YouTube("https://www.youtube.com/watch?v=_pzu-Z1gbqU")
stream=video.streams.get_highest_resolution()
stream.download()