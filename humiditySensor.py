import os
import csv
import Adafruit_DHT
import time
from datetime import datetime

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

def append_list_as_row(file_path, data,keys):
    # Open file in append mode
    file_name=os.path.join(file_path,data["datetime"].strftime("%m%d%Y")+".csv")
    if not os.path.exists(file_name):
        with open(file_name, "w") as f:
            writer = csv.DictWriter(f,fieldnames=keys)
            writer.writeheader()
            writer.writerow(data)
    else:
        with open(file_name, 'a+', newline='') as f:
            writer = csv.DictWriter(f,fieldnames=keys)
            writer.writerow(data)


keys=["datetime","temperature","humidity"]
while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        timenow=datetime.now()
        datapoint={"datetime":timenow,"temperature":temperature,"humidity":humidity}
        append_list_as_row("/home/pi/humidityMonitor/data",datapoint,keys)
        print("time: ",datapoint["datetime"].strftime("%H:%M:%S"),", Temp ",temperature, ", humidity:", humidity)
    else:
        print("Sensore failure, Check wiring.");
    time.sleep(60);
