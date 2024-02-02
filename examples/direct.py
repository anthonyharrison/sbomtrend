import json
import matplotlib.pyplot as plt

filename="/tmp/cvebin.json"

with open(filename) as file:
    data=json.load(file)

depfilename="/tmp/latest_requirements.txt"

with open(depfilename) as file:
    file_contents=file.read().splitlines()

# Remove non package name characters (order matters...)
contents=[]
for f in file_contents:
    if "[" in f:
        contents.append(f.split("[", 1)[0])
    elif ">" in f:
        contents.append(f.split(">", 1)[0])
    elif ";" in f:
        contents.append(f.split(";",1)[0])
    elif "<" in f:
        contents.append(f.split("<", 1)[0])
    else:
        contents.append(f)

print (contents)

# Get all the dates. Assume first entry covers all dates of interest
date={}
for package in data["packages"].keys():
    for version_history in data["packages"][package]["version_history"].keys():
        date[version_history]=0
    break

x= []
for d in date:
    print(f",{d}", end="")
    x.append(d)

plt.figure(figsize=(20,12))
plt.xticks(rotation=90)

# Process each package and identify
for package in data["packages"].keys():
    #print (f"\n{package}",end="")
    for version_history in data["packages"][package]["version_history"].keys():
        date[version_history] = data["packages"][package]["version_history"][version_history]

    # Only show direct dependencies
    if package in contents:
        print(f"Direct dependency {package}")
        package_data=[]
        for d in date:
            #print (f",{date[d]}", end="")
            package_data.append(date[d])
            # reset to mark entry as unused
            date[d]=0
        plt.plot(x, package_data, label=package)

plt.grid(axis='x', color='0.95')
plt.grid(axis='y', color='0.95')
plt.legend(loc='upper left', title='Packages')
plt.title('Package Version Analysis - Direct Dependencies')
plt.savefig("/tmp/direct.png")

