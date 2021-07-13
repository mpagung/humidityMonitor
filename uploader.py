import pandas as pd

keys=["datetime","temperature","humidity"]
filepath = "/home/pi/humidityMonitor/data"
file_name=os.path.join(file_path,data["datetime"].strftime("%m%d%Y")+".csv")

data = pd.read_csv (file_name)
df = pd.DataFrame(data, columns= keys)
#check and upload every noon and 2359
print(df)
