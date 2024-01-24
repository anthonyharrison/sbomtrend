from lib4package.metadata import Metadata
import json
import matplotlib.pyplot as plt
import datetime as dt

filename="/tmp/cvebin.json"

with open(filename) as file:
    data=json.load(file)

#
#
# filename="/tmp/packages.txt"
#
# with open(filename) as f:
#     package_list = f.readlines()
#
# # Remove new lines
# package_list = [x.strip() for x in package_list]
# for package in package_list:
#     pm.get_package(package)
#     last_update = pm.get_latest_release_time()
#     print (f"{package}, {last_update}")

fig, ax = plt.subplots(figsize=(20,12), layout='constrained')
update=[]
packages=[]
colour=[]

pm = Metadata()
# Process each package and identify
for package in data["packages"].keys():

    if data["packages"][package]["versions"] == 1:
        # No updates
        pm.get_package(package)
        last_update = dt.datetime.strptime(pm.get_latest_release_time()[:10],'%Y-%m-%d').date()
        if last_update < dt.date(2022, 1, 1):
            colour.append('red')
        else:
            colour.append('blue')
        update.append(last_update)
        packages.append(package)

ax.barh(packages, update, color=colour, align='center')
labels = ax.get_xticklabels()
plt.setp(labels, horizontalalignment='right')
ax.set(xlim=[dt.date(2018, 1, 1), dt.date(2025,1,1)], xlabel='Date of last update', ylabel='Package',
       title='Date of Last Update of Package')
plt.grid(axis='x', color='0.95')
plt.savefig("/tmp/age.png")