from tkinter import *
from tkinter import messagebox
import pyperclip
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    letters_list = [ password_list.append(random.choice(letters)) for char in range(nr_letters)]
    symbols_list = [ password_list.append(random.choice(symbols)) for char in range(nr_symbols) ]
    numbers_list = [ password_list.append(random.choice(numbers)) for char in range(nr_numbers) ]

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    if len(website)==0 and len(password) == 0 :
        messagebox.showerror(title="Oops", message="Website or Username field cannot be empty.")
    else:
        is_ok=messagebox.askokcancel(title = website , message = f"These are the details you entered:\n Username: {username} \n Password: {password} \n Is it Ok to Save?")
        if is_ok:
            with open("password-manager-start\\data.txt","a") as password_data:
                password_data.write(f"{website} | {username} | {password} \n")
                website_entry.delete(0,END)
                username_entry.delete(0,END)
                password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title=("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(width=200,height=200)
password_img = PhotoImage(file="password-manager-start\\logo.png")
canvas.create_image(100,100,image=password_img)
canvas.grid(column=1,row=0)

website_label = Label(text="Website: ")
website_label.grid(column=0,row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1,row=1, columnspan=2)
website_entry.focus()

username_label = Label(text="Email/Username: ")
username_label.grid(column=0,row=2)

username_entry = Entry(width=35)
username_entry.grid(column=1,row=2 , columnspan=2)


password_label = Label(text="Password: ")
password_label.grid(column=0,row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1,row=3)

generate_button_label = Button(text="Generate Password",command=generate_password)
generate_button_label.grid(column=2,row=3)
 
add_button_label = Button(width=36,text="Add",command=save)
add_button_label.grid(column=1,row=4,columnspan=2)

window.mainloop()