'''
Files like this will be present in data folder ▶ channelName_date_time_year_
700 - all files
13 - channel names
if(filename.startswith(channelname)) -->collect display it to the user
Choose File 1
display the list and ask press 
1. 3jan 
2. 5jan 
.
.
.....

Choose File 2
display the list and ask press 
1. 3jan 
2. 5jan 
.
.
.....

outputs/channel_date1_date2.xlsx
title date1 date2 view_count(difference)
..
..
..

'''

import json
import os
import questionary

list_of_channels = os.listdir("outputs/")

channel_name = questionary.select("Enter channel name: ", choices = list_of_channels).ask()
list_of_files = os.listdir(f"outputs/{channel_name}")

while True:
    files_chosen = questionary.checkbox("Choose two files by clicking spacebar: ", choices = list_of_files).ask()
    if len(files_chosen)==2:
        break
    else:
        print("Choose two files")

print(files_chosen)

"""

DON'T SEE ANY NEED YET

def get_date(filename: str):
    return int(filename.split(" ")[0].replace("-", ""))

dates = list(map(get_date, files_chosen))
dates.sort()
print(dates)

"""

with open(f"outputs/{channel_name}/{files_chosen[0]}", "r") as f1:
    old_data = f1.read()

with open(f"outputs/{channel_name}/{files_chosen[1]}", "r") as f2:
    new_data = f2.read()

old_data = json.loads(old_data)
new_data = json.loads(new_data)

data = {
    "Video ID": [],
    "Video Title": [],
    "Difference In Views": []
}

for i in new_data:
    # print()

    difference_in_views = 0

    for j in old_data:
        if i['Video ID']==j['Video ID']:
            
            difference_in_views = i['Views']-j['Views']
    
    if difference_in_views == 0:
        difference_in_views = "New video uploaded"
    
    data['Video ID'].append(i['Video ID'])
    data['Video Title'].append(i['Video Title'])
    data['Difference In Views'].append(difference_in_views)

import pandas as pd

data = pd.DataFrame(data)
try:
    data.to_excel(f"data/{channel_name}/{files_chosen[0][:10]} {files_chosen[1][:10]}.xlsx", index=False)
except:
    try:
        from os import mkdir
        mkdir(f"data/{channel_name}")
    except:
        pass
    data.to_excel(f"data/{channel_name}/{files_chosen[0][:10]} {files_chosen[1][:10]}.xlsx", index=False)