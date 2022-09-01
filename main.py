from pytube import YouTube
import pytube
from prettytable import PrettyTable
import sys

try:
    link = ""
    print("Press Ctrl C if u want to EXIT.")
    try:
        try:
            link = YouTube(sys.argv[1])
        except pytube.exceptions.RegexMatchError:
            while (True):
                try:
                    link = YouTube(input("Enter your link again: "))
                    break
                except pytube.exceptions.RegexMatchError:
                    pass
    except IndexError:
        try:
            link = YouTube(input("Link: "))
        except pytube.exceptions.RegexMatchError:
            while (True):
                try:
                    link = YouTube(input("Enter your link again: "))
                    break
                except pytube.exceptions.RegexMatchError:
                    pass
    try:    
        downloadList = link.streams
    except pytube.exceptions.VideoUnavailable:
        print('Oops. This video is unavailable.')
        exit()
    tableDownloadList = PrettyTable(["No. ", "itag", "resolution", "fps/abr", "type", "has audio", "file type", "bitrate", "codecs", "3D"])
    for item in downloadList:
        if (hasattr(item, 'fps')):
            tableDownloadList.add_row([downloadList.index(item)+1, item.itag, item.resolution, item.fps, item.type, item.is_progressive, item.mime_type.replace("video/", ""), item.bitrate, item.codecs, item.is_3d])
        else:
            tableDownloadList.add_row([downloadList.index(item)+1, item.itag, item.resolution, item.abr, item.type, "", item.mime_type.replace("audio/", ""), item.bitrate, item.codecs, ""])
    print(tableDownloadList)
    downloadList[int(input("\nEnter number you want to download: "))-1].download()
    print("Download successfully.")
except KeyboardInterrupt:
    print('Goodbye (:')