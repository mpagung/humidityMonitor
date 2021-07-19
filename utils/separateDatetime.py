#Function: separate date and time of old sensor recording
import datetime
import os
import csv
from tkinter import filedialog as fd
import pandas as pd

# datetime.strptime(date_string)


# filepath = fd.askdirectory(title="Select Data Folder",initialdir="./")
filepath = 'C:/Users/micha/Documents/GitHub/humData'
if filepath :
    filenames=os.listdir(filepath)
    newfilepath=os.path.join(filepath,"converted") #filepath for saving converted file

    if not os.path.exists(newfilepath):
        os.makedirs(newfilepath)

    keys= pd.read_csv(os.path.join(filepath,filenames[0]), index_col=0, nrows=0).columns.tolist() # get lit of pre-existing keys
    #note to self, since datetime is index, datetime will not be in keys automatically
    keys.insert(0,"date")
    keys.insert(1,"time")

    for filename in filenames:
        df = pd.read_csv(os.path.join(filepath,filename))
        dateNtime = df["datetime"]
        date=[]
        time=[]
        for entry in dateNtime:
            timepoint=datetime.datetime.strptime(entry,'%Y-%m-%d %H:%M:%S.%f')
            date.append(timepoint.strftime("%m/%d/%Y"))
            time.append(timepoint.strftime("%H:%M:%S.%f"))
        df["date"]=date
        df["time"]=time

        with open(os.path.join(newfilepath,"b"+filename), "w") as f:
            df.to_csv(f, columns=keys)
        # with open(os.path.join(newfilepath,filename), "w") as f:
        #     writer = csv.DictWriter(f,fieldnames=keys)
        #     writer.writeheader()
        #     writer.writerow(df)
else:
    print("You did not select a folder, please try again")
