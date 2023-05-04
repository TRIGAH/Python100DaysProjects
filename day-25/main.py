import csv
import pandas    

data = pandas.read_csv("day-25\\weather-data.csv") 

# data_dict = data.to_dict() 
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# temp_avg = data["temp"].mean()
# print(temp_avg)
import pandas
squirrel_data = pandas.read_csv("day-25\\228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
# print(squirrel_data["Primary Fur Color"])
# print(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])

gray_count = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
cinnamon_count = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]
black_count = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]

print(gray_count["Primary Fur Color"].count())
print(cinnamon_count["Primary Fur Color"].count())
print(black_count["Primary Fur Color"].count())

squirrel_data_dict = {
    "Fur Color":["Gray","Cinnamon","Black"],
    "count":[gray_count["Primary Fur Color"],cinnamon_count["Primary Fur Color"],black_count["Primary Fur Color"]]
}

data = pandas.DataFrame(squirrel_data_dict)
data.to_csv("day-25\\squirrel_count.csv")