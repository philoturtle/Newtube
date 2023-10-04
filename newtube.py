import argparse
import pytube
import re


parser = argparse.ArgumentParser(description= 'This program is downloading video from YouTube')
parser.add_argument("-l","--link", help="downloading the video from input url")
args = parser.parse_args()
link = args.link

pattern = 'youtube.com'
result = re.match(pattern, link)
if result:
	print('Downloading the video in  progress')
else:
	print('Error: Wrong url. Use --help')
	exit(1)
	
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download('/mnt/c/Users/mmusz/Downloads')
print('Video downloaded')
