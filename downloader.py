import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import json

load_dotenv("./.env")
mongoCredentials = os.getenv("MONGO_CLIENT")

#Connection to mongoose
client = MongoClient(mongoCredentials)
database = client["HumidityProto"]
collection = database['Reading']

#convert mongoose json to pandas
res=collection.find()
# data = json.loads(res)
# df = pd.json_normalize(data)
print(pd.DataFrame(list(res)))
