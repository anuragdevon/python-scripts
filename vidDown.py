#!usr/bin/python3
# simpler youtube downloader 
#  /usr/bin/python3 /home/anurag/Documents/automations/ytd.py
from pytube import YouTube
link = input("\nEnter: ")
vid = YouTube(link)
print(vid.streams.filter(progressive=True))
print("\ntag: ")
tag = int(input())
stored = vid.streams.get_by_itag(tag)
stored.download()
# https://www.youtube.com/watch?v=4RWFvXDUmjo
