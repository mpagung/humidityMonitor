from pymongo import MongoClient
from dotenv import load_dotenv
import os

def mongoconnect(dotenv_filepath):
    #function: connect to mongodb and return the collection for humidity Sensor
    load_dotenv(dotenv_filepath)
    mongoCredentials = os.getenv("MONGO_CLIENT")

    client = MongoClient(mongoCredentials)
    database = client["HumidityProto"]
    collection = database['Reading']

    return(collection)
