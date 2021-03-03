import csv
from datetime import datetime
import matplotlib.pyplot as plt

open_file = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

for index, column_header in enumerate(header_row):
    print("Index:", index, "Column Name:", column_header)

highs = []
dates = []
lows = []
for row in csv_file:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(converted_date)

# print(highs)

fig = plt.figure()

plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")

# fig.autofmt_xdate()

fill = plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

plt.title("Daily high and low temperatures - 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", labelsize=12)

# plt.show()


open_file = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

for index, column_header in enumerate(header_row):
    print("Index:", index, "Column Name:", column_header)

highs1 = []
dates1 = []
lows1 = []
for row in csv_file:
    try:
        high = int(row[4])
        low = int(row[5])
        converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    except ValueError:
        print(f"missing data for {converted_date}")
    else:
        highs1.append(high)
        lows1.append(low)
        dates1.append(converted_date)
# print(highs)

fig = plt.figure()

plt.plot(dates1, highs1, c="red")
plt.plot(dates1, lows1, c="blue")


fig.autofmt_xdate()

plt.fill_between(dates1, highs1, lows1, facecolor="blue", alpha=0.1)

plt.title("Daily high and low temperatures - 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", labelsize=12)

# plt.show()


fig2, a = plt.subplots(2)

fig2.suptitle(
    "Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLY, CA US"
)
a[0].fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
a[0].plot(dates, highs, c="red")
a[0].plot(dates, lows, c="blue")
a[0].title.set_text("SITKA AIRPORT, AK US")
# a[0].title("Daily high and low temperatures - 2018", fontsize=16)

a[1].plot(dates, highs1, c="red")
a[1].plot(dates, lows1, c="blue")
plt.fill_between(dates1, highs1, lows1, facecolor="blue", alpha=0.1)
a[1].title.set_text(
    "DEATH VALLY, CA US",
)
plt.show()