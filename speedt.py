import speedtest
import csv
import datetime
import os.path
from os import path

"""A quick script for checking internet speed.
My ISP is not reliable and expensive, so I'm checking speed once an hour.
I'll add feature to automatically send message to ISP with results.

"""

def speed_test():
    servers = []

    threads = 1

    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download(threads=threads)
    s.upload(threads=threads)
    s.results.share()

    results_dict = s.results.dict()

    return results_dict

def save_result(file_name):
    results = {}

    data = speed_test()
    #in_mb = 0.145
    in_mb = data['download']/8000000
    up_mb = data['upload']/8000000
    in_kb = data['download']/1024
    print('MBps is {0:.3f}'.format(in_mb))
    print('KBps is {0:.3f}'.format(up_mb))
    timestamp = datetime.datetime.now()
    t = timestamp.strftime("%m/%d/%Y %H:%M:%S")

    results.update(timestamp = t, download_speed = round(in_mb, 3), upload_speed = round(up_mb, 3))

    """checking if file to write into exists,
    its my quick and dirty solution to write rows with keys only once...
    if exists > append, else > open in write mode.
    """

    if path.exists(file_name):
        with open(file_name, mode='a', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(results.values())

    else:
        with open(file_name, mode='w', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(results.keys())
            writer.writerow(results.values())


save_result('result.csv')
