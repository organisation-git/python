import csv
from collections import Counter
with open('height-weight.csv', newline='') as file:
    reader = csv.reader(file)
    file_data = list(reader)

file_data.pop(0)
new_data = []
mode_new_data = []

for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))
    mode_new_data.append(n_num)

n = len(new_data)
new_data.sort()

total = 0
for x in new_data:
    total += x

mean = total/n

if n % 2 == 0:
    median1 = float(new_data[n//2])
    median2 = float(new_data[n//2-1])
    median = (median1+median2)/2
else:
    median = new_data[n//2]


data = Counter(new_data)
md = {
    "65-75": 0,
    "75-85": 0,
    "85-95": 0
}
for height, occ in data.items():
    if 50 < float(height) < 60:
        md['65-75'] += occ
    elif 60 < float(height) < 70:
        md['75-85'] += occ
    elif 70 < float(height) < 80:
        md['85-95'] += occ

mode_range, mode_occ = 0, 0
for range, occ in md.items():
    if occ > mode_occ:
        mode_range, mode_occ = [
            int(range.split("-")[0]), int(range.split("-")[1])], occ

mode = float((mode_range[0]+mode_range[1])/2)

print(f"mode is {mode:2f}")
print(f"median is {median}")
print(f"mean is {mean}")
