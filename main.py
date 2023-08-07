
# with open("weather_data.csv", mode="r") as data:
#   list_weather = data.readlines()
#   no_line = [x.rstrip() for x in list_weather]

# print(no_line)

########################################################
# import csv

# with open("weather_data.csv", mode="r") as data:
#   # creates a csv reader object
#   data = csv.reader(data)
#   temperatures = []
#   for row in data:
#     if row[1] != "temp":
#       temperatures.append(int(row[1]))
#     # print(row)
#     # for items in row:
#     #   temperatures.append(items.split(','))

#   print(temperatures)

# SIDE QUEST
# with open("weather_data.csv", mode="r") as data:
#   data = csv.reader(data)
#   temperatures = []
#   for row in data:
#     if row[1] != "temp":
#       for x in (range(len(row)-1)):
#         if x == 1:
#           temperatures.append(int(row[x]))
#     # for items in row:
#     #   print(items)
#     #   # if row != "temp":
#     #   temperatures.append(items.split(','))

# print(temperatures)

import pandas
data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# # print(data_dict)

# from statistics import mean 
# temp_list = data["temp"].to_list()
# print(mean(temp_list))
# print(sum(temp_list) / len(temp_list))
# #OR use series methods, series are like the columns
# print(data["temp"].mean())
# print(data["temp"].max())

# # same but dont need to worry about typos, wont run if column name doesnt match
# print(data["condition"])
# print(data.condition)

# # get data in row
# print(data[data.day == "Monday"])
# # row where temperature was max
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)
# # monday.temp = (monday.temp * 9 / 5) + 32
# # print(monday.temp)

# create a data frame from scratch
data_dict = {
  "students": ["amy", "james", "angela"],
  "scores": [76, 56, 65],
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
