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

# data = pandas.read_csv("weather_data.csv")
# #print(data["temp"])
#
# data_dict = data.to_dict()
# #print(data_dict)
#
# temp_list = data["temp"].to_list()
# #print(f"Average of temperature: {round(sum(temp_list) / len(temp_list), 1)}")
# # print(f"Average of temperature: {round(data['temp'].mean(), 1)}")
# # print(f"Maximum of temperature: {data['temp'].max()}")
#
# # print(data[data['day'] == 'monday'])
# # print(data[data.temp == data.temp.max()])
#
# def TempCtoF(Celsius):
#     Celsius = float(Celsius)
#     Fahrenheit = float((9/5 * Celsius)+ 32)
#     return Fahrenheit
#
# monday = data[data.day == 'Monday']
#
# data_dict = {
#     "Students": ["changhun", "mikyoung", "jonggon"],
#     "Score": [100, 90, 80]
# }
#
# data_pandas = pandas.DataFrame(data_dict)
# print(data_pandas)
# data_pandas.to_csv("new_csv_file")



