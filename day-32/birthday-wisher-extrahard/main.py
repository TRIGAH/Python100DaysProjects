import datetime as dt
import pandas
import random
import smtplib


MY_EMAIL = "ijenrandy2@gmail.com"
MY_PASSWORD = "conjgpvrczhkxlqo"
letter_to_send = ""

all_letters=["letter_1.txt","letter_2.txt","letter_3.txt"]
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
birthday_file=pandas.read_csv("day-32\\birthday-wisher-extrahard\\birthdays.csv")
now = dt.datetime.now()
today = now.weekday()

birth_name=birthday_file[birthday_file.day == today]
name=birth_name.name.to_list()[0]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
chosen_letter = random.choice(all_letters)
print(chosen_letter)

with open(f"day-32\\birthday-wisher-extrahard\\letter_templates\\{chosen_letter}","r") as letters:
        letter = letters.read() 
        letter_to_send = letter.replace('[NAME]',f"{name}")          

# 4. Send the letter generated in step 3 to that person's email address.
with smtplib.SMTP_SSL("smtp.gmail.com",465) as connection:
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{letter_to_send}"
        )
