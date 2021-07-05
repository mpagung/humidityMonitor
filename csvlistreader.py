import csv

def csvlistreader(filename):
    with open(filename,"r") as f:
        csvlist=[]
        for row in f:
            csvlist.append(row)
    return(csvlist)

list1=csvlistreader("07052021rec.csv")

print(list1[0])


