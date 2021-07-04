import os
from csv import writer
import Adafruit_DHT
import time
from datetime import datetime

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    if not os.path.exists(file_name):
	with open(file_name, "w") as f:
	   f.write(list_of_elem)
    else: 
	with open(file_name, 'a+', newline='') as write_obj:
            csv_writer = writer(write_obj)
            csv_writer.writerow(list_of_elem)


while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        timenow=datetime.now()
        data="Temp={0:0.1f}C, Humidity={1:0.1f}%".format(temperature, humidity);
        append_list_as_row(test.csv, [timenow,data])
        print(timenow,data)
    else:
        print("Sensore failure, Check wiring.");
    time.sleep(5);
