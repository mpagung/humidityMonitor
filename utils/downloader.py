import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import json
from mongoconnect import mongoconnect

def downloader(filename):
    #Function: Connect to mongodb and get data collection from mongodb
    collection=mongoconnect("./.env")

    #convert mongoose json to pandas
    res=collection.find()
    print(pd.DataFrame(list(res)))
    return(res)
