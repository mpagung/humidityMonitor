import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import json
from mongoconnect import mongoconnect 

### initial params
# keys=["datetime","temperature","humidity"]
#filepath = "/home/pi/humidityMonitor/data" #for linux
#file_name=os.path.join(file_path,data["datetime"].strftime("%m%d%Y")+".csv")
#filepath="./" #for windows testing

#Connection to mongoose
collection=mongoconnect("./.env")


file_name ="../humData/07102021.csv"

data = pd.read_csv (file_name)
# df = pd.DataFrame(data, columns= keys)
df=json.loads(data.to_json(orient='records'))

collection.insert_many(df)
#check and upload every noon and 2359
# print(df)
