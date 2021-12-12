from typing import ClassVar


import csv
import math
with open("data.csv", newline= '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def mean(data) :
    n= len(data)
    total = 0
    for i in data:
        total = total + float(i)
    
    mean = total/n
    return mean

squared_list= []
for number in data:
    x = int(number) - mean(data)
    x = x**2
    squared_list.append(x)

sum = 0
for d in squared_list:
    sum = sum + d

result = sum/(len(data) - 1)

std_deviation = math.sqrt(result)
print(std_deviation)