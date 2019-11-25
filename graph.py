from datetime import datetime
import csv
import pygal


download_sp = []
upload_sp = []
timestamp = []


with open('result.csv', mode = "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for item in reader:
        download_sp.append(float(item['download_speed']))
        upload_sp.append(float(item['upload_speed']))
        timestamp.append(datetime.strptime(item['timestamp'], '%m/%d/%Y %H:%M:%S'))


#print(timestamp)

date_chart = pygal.Line(x_label_rotation=20)
date_chart.x_labels = map(lambda d: d.strftime('%m-%d %H:%M'), timestamp)
date_chart.add('download', download_sp)
date_chart.add('upload', upload_sp)
date_chart.render_in_browser()
