import argparse
import pytube

parser = argparse.ArgumentParser(description= 'This program is downloading video from YouTube')
parser.add_argument("-l","--link", help="downloading the video from input url")
args = parser.parse_args()
if args.link:
	print("Downloading the video in progress")

link = args.link
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download('/mnt/c/Users/mmusz/Downloads')
print('Video downloaded')
