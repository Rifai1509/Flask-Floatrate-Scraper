import requests
import csv

source = requests.get('http://www.floatrates.com/daily/usd.json')
json_data = source.json().values()
datas=[]
for data in json_data:
    name = data['name']
    date =data['date']
    invers=data['inverseRate']
    # print("Name :",name)
    # print("Date :",date)
    # print("Invers Rate:",invers)
    datas.append([name, date, invers])

# print(datas)
writer = csv.writer(open('FloatRates.csv', 'w', newline='', encoding="utf-8"))
headers = ['Name', 'Date', 'Invers Rates']
writer.writerow(headers)
for data in datas:
    print(data)
    writer.writerow(data)