import pytube
link = "https://www.youtube.com/watch?v=wwux9KiBMjE"
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download('/mnt/c/Users/mmusz/Downloads')
print('Video downloaded')
