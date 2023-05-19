
# try:
#     file = open("day-30\\darta.txt","r")
#     file.read()

#     a_dictinary = {"key":"value"}
#     print(a_dictinary["key"])   
# except FileNotFoundError:
#     file = open("day-30\\darta.txt","w")
#     file.write("Hope is REAL")
# except KeyError:
#     a_dictinary = {"key":"value"}
#     print(a_dictinary["key"])

# else:
#     file = open("day-30\\darta.txt","r")
#     print(file.read())
   
# finally:       
#     print("Operation Successful") 



# fruits = ["Apple", "Pear", "Orange"]

# #TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print(f"Fruit Pie")
#         print(f"The index {index} does not exist")
#     else:
#         print(fruit + " pie")


# make_pie(4)


facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass
    
print(f"This profile has {total_likes} total likes on posts")


