import subprocess as sp
import json
from datetime import datetime
from os import mkdir
from time import sleep

playlists = ["PLu0W_9lII9agtWvR_TZdb_r0dNI8-lDwG", "PLu0W_9lII9ahwFDuExCpPFHAK829Wto2O"]
# playlists = ["UU7iCj6RpJlRL4iPac_Ca9SA"]
timestamp = datetime.now()
timestamp = str(timestamp).replace(':', '_').split('.')[0]

for count, playlistId in enumerate(playlists):
    sleep(1800)
    totalData = []

    # a = sp.getoutput('youtube-dl -s --print-json --write-info-json https://www.youtube.com/watch?v=PIUnwYYBEnw')
    print(f"{count}: {playlistId}")
    a = sp.getoutput(f'youtube-dlc -s --print-json --write-info-json https://www.youtube.com/playlist?list={playlistId}')
    a = a.replace('\n{"id":', ',\n{"id":')
    a = '[' + a + ']'
    all = json.loads(a)

    # b = json.loads(a)['view_count']
    # print(b)
    for i in all:
        data = {
            "Video ID": i['id'],
            "Video Title": i['title'],
            "Views": i['view_count'],
        }
        totalData.append(data)
    

    channelName = i['uploader']
    try:
        with open(f"outputs/{channelName}/{timestamp}.json", 'w') as f:
            f.write(json.dumps(totalData))
    except:
        mkdir(f"outputs/{channelName}")
        with open(f"outputs/{channelName}/{timestamp}.json", 'w') as f:
            f.write(json.dumps(totalData))
    
    # with open("data/{channelName_date_time_year}.json", 'w') as f:
    #     f.write(str(a))