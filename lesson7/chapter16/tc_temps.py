import csv
import matplotlib.pyplot as plt
from datetime import datetime

days = [] # col 2
tempH = [] # col 3
tempL = [] # col 4

with open("lesson7/chapter16/2905706.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    headers = next(csv_reader)
    for row in csv_reader:
        # check if HIGH and LOW are both recorded by this station on this row
        if row[3] != "" and row[4] != "":
            days.append(datetime.strptime(row[2], "%Y-%m-%d"))
            tempH.append(int(row[3]))
            tempL.append(int(row[4]))


plt.scatter(days, tempH, c="red", label="High")
plt.scatter(days, tempL, c="blue", label="Low")
plt.xticks(rotation=25)
plt.xlabel("Date")
plt.ylabel("Temperature (F)")
plt.legend(loc="best")
plt.suptitle("Traverse City Temperature Ranges")
plt.title("Jan 1 through Mar 14 (Present)")

plt.show()
