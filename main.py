from pytube import YouTube
from prettytable import PrettyTable

link = YouTube(input("Link: "))
downloadList = link.streams
tableDownloadList = PrettyTable(["No. ", "itag", "resolution", "fps/abr", "type", "has audio", "file type", "bitrate", "codecs", "3D"])
for item in downloadList:
    if (hasattr(item, 'fps')):
        tableDownloadList.add_row([downloadList.index(item)+1, item.itag, item.resolution, item.fps, item.type, item.is_progressive, item.mime_type.replace("video/", ""), item.bitrate, item.codecs, item.is_3d])
    else:
        tableDownloadList.add_row([downloadList.index(item)+1, item.itag, item.resolution, item.abr, item.type, "", item.mime_type.replace("audio/", ""), item.bitrate, item.codecs, ""])
print(tableDownloadList)
downloadList[int(input("\nEnter number you want to download: "))-1].download()
print("Download successfully.")