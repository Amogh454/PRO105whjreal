
import statistics
import math
import csv

from numpy import append

with open('data.csv',newline='') as f:
    r=csv.reader(f)
    fileData=list(r)

data = fileData[1]    

def mean(data):
    n=len(data)
    sum=0
    for i in data:
        sum = sum+int(i)
        

    mean = sum/n
    return mean

list1 = []

for x in data:
    s = int(x)-mean(data)
    s = s**2 
    list1.append(s)

total = 0
for j in list1:
    total = total+j

result = total / len(data)-1

std = math.sqrt(result)
print(std)

