# with open("weather_data.csv") as weather_file:
#     data = weather_file.readlines()
# for day_data in data:
#     day_data_stripped = day_data.strip()
#     data_with_space = day_data_stripped.replace(",", " ")
#     print(data_with_space)

# import csv
# with open("weather_data.csv") as weather_file:
#     data = csv.reader(weather_file)
#     # data 는 open 된 file 이 close 되긴 전까지만 유효한 듯!!!
#     temperature = []
#
#     for row in data:
#         # isdigit 말고 isnum은 왜 안 됨?
#         if row[1].isdigit():
#             temperature.append(int(row[1]))
#
#     print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])
