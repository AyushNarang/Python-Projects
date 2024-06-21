# with open("weather_data.csv") as w_data:
#     w_list = w_data.readlines()
#
# print(w_list)

# import csv
#
# with open("weather_data.csv") as datafile:
#     data_obj = csv.reader(datafile)
#     temperature = []
#     for row in data_obj:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# temp_list = data["temp"].to_list()
#
# print(data["temp"].max())

# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# temp = (monday.temp[0] * (9/5)) + 32
# print(temp)

data_dict = {"user": ["A", "B"],
             "age": [8, 9]
             }
data = pandas.DataFrame(data_dict)
# data.to_csv("Test.csv")

# Loop through DataFrame
for (index, row) in data.iterrows():
    if row.user == "A":
        print(row.age)