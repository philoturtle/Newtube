import argparse
import pytube
import re
import typing

# zrób klase
# podziel na funkcje
# jak używać if __name__ == "__main__"


class YTFilm:
    def __init__(self, link: str) -> str:
        self.link = link
        self.downloaded_film = pytube.YouTube(link)

    def downloading(self) -> str:
        stream = self.downloaded_film.streams.first()
        stream.download("/mnt/c/Users/mmusz/Downloads")
        print("Video downloaded")

    def url_check(self) -> bool:
        result = re.search(r"youtube\.com", self.link)
        if result:
            print("Downloading the video in  progress")
            return True
        else:
            print("Error: Wrong url. Use --help", result)
            return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="This program is downloading video from YouTube"
    )
    parser.add_argument("-l", "--link", help="downloading the video from input url")
    args = parser.parse_args()
    link = args.link
    ytfilm = YTFilm(link)
    if ytfilm.url_check():
        ytfilm.downloading()
