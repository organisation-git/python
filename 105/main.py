import csv
import math

with open('main.csv', 'r') as file:
    reader = csv.reader(file)
    file_data = list(reader)


data = file_data[0]


def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)

    mean = total/n
    return mean


squared_list = []
meansize = mean(data)
for n in data:
    a = int(n) - meansize
    a = a**2
    squared_list.append(a)

sum = 0
for i in squared_list:
    sum += i


result = sum/(len(data)-1)
stddeviation = math.sqrt(result)

print(f"std deviatio {stddeviation}")
