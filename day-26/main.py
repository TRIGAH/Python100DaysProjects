import pandas
# file1_data = []
# file2_data = []
# result = []
# with open("day-26\\file1.txt") as file1:
#     data = file1.readlines()
#     file1_data = [int(num.replace("\n","")) for num in data]
# with open("day-26\\file2.txt") as file2:
#     data = file2.readlines()
#     file2_data = [int(num.replace("\n","")) for num in data]

# result = [num1 for num1 in file1_data  if num1 in file2_data]

# # Write your code above 👆

# print(result)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
# words_list = sentence.split(" ")
# result = {word:len(word) for word in words_list}

# # Write your code below:



# print(result)


# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }

# # 🚨 Don't change code above 👆
# weather_f = {day:temp_c * 9/5 + 32 for (day,temp_c) in weather_c.items()}
# # Write your code 👇 below:
# print(weather_f)

student_dict = {
    "Student": ["Angela","Maps","Lily"],
    "Score": [90,34,68]
}
student_data = pandas.DataFrame(student_dict)
print(student_data)

for (index,row) in student_data.iterrows():
    print(row.Score)
