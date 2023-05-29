import datetime as dt
import pandas

all_letters=[]
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
birthday_file=pandas.read_csv("day-32\\birthday-wisher-extrahard\\birthdays.csv")
now = dt.datetime.now()
today = now.weekday()
if today in birthday_file.day:
    print("Yes it does")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
for x in range(1,4):
   with open(f"day-32\\birthday-wisher-extrahard\\letter_templates\\letter_{x}.txt","r") as letter:
          

  


# 4. Send the letter generated in step 3 to that person's email address.


