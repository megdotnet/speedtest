#!/usr/bin/env python3

import datetime
import os

date = datetime.datetime.now().strftime("%m%d%y")
filename = "speedtest_" + date + ".csv"

os.system('speedtest -p --progress=no --unit=Mbps --format=csv > output.txt')

with open('output.txt', 'r') as data:
    for line in data: 
        server_name = line.split("\",\"")[0]
        server_id = line.split("\",\"")[1]
        latency = line.split("\",\"")[2]
        jitter = line.split("\",\"")[3]
        packet_loss = line.split("\",\"")[4]
        download = float(line.split("\",\"")[5][0:4])/100
        upload = float(line.split("\",\"")[6][0:4])/100
        download_bytes = float(line.split("\",\"")[7][0:3])/10
        upload_bytes = float(line.split("\",\"")[8][0:3])/10
        share_url = line.split("\",\"")[9] 
        download_server_count = line.split("\",\"")[10]
        timestamp = datetime.datetime.now().strftime("%H:%M")

if not os.path.exists(filename):
    file = open(filename, "w")
    file.write('"Server Name","Server ID","Latency","Jitter","Packet Loss","Down Mbps","Up Mbps","Timestamp"\n')
    file.close()

file = open(filename, "a")
write_data = ('"' + server_name.strip('"') + '","' + server_id + '","' + latency + '","' + jitter + '","' + packet_loss + '","' + str(download) + '","' + str(upload) + '","' + timestamp + '"\n')
file.write(write_data)
file.close()
