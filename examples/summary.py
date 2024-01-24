import json
import matplotlib.pyplot as plt

filename="/tmp/cvebin.json"

with open(filename) as file:
    data=json.load(file)

x=[]
change=[]
count=[]
for date in data["package_data"].keys():
    x.append(date)
    change.append(data['package_data'][date]['change'])
    count.append(data['package_data'][date]['count'])

plt.figure(figsize=(20,12))
plt.plot(x, count, marker = 'o', color='green',label='count')
plt.plot(x, change, marker = '+', color='red', label='change')
plt.xticks(rotation=90)
plt.grid(axis='x', color='0.95')
plt.grid(axis='y', color='0.95')
plt.legend(title='Parameters')
plt.title('Package Analysis')
plt.savefig("/tmp/summary.png")

