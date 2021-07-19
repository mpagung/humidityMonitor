import os
import csv
import Adafruit_DHT
import time
from datetime import datetime

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

#Function: continuously read sensor and insert datapoint to csv file

def append_list_as_row(file_path, data,keys):
    # Open file in append mode
    file_name=os.path.join(file_path,"b"+datetime.strptime(data["date"],"%m/%d/%Y").strftime("%m%d%Y")+".csv")
    if not os.path.exists(file_name):
        with open(file_name, "w") as f:
            writer = csv.DictWriter(f,fieldnames=keys)
            writer.writeheader()
            writer.writerow(data)
    else:
        with open(file_name, 'a+', newline='') as f:
            writer = csv.DictWriter(f,fieldnames=keys)
            writer.writerow(data)


keys=["date","time","temperature","humidity"]
filepath="/home/pi/humidityMonitor/data"
while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        timenow=datetime.now()
        datapoint={"date":timenow.strftime("%m/%d/%Y"),"time":timenow.strftime("%H:%M:%S.%f"),"temperature":temperature,"humidity":humidity}
        append_list_as_row(filepath,datapoint,keys)
        print("time: ",datetime.strptime(datapoint["time"],"%H:%M:%S.%f").strftime("%H:%M:%S"),", Temp ",temperature, ", humidity:", humidity)
    else:
        print("Sensore failure, Check wiring.");
    time.sleep(60);
