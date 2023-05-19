from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import json
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
def find_password():
    website = website_entry.get()
    try:
        with open("password-manager-start\\data.json","r") as password_data:
            data=json.load(password_data)
    except FileNotFoundError:   
        messagebox.showerror(title="404", message=f"No data file found ")     
    else:
        for web in data:
            if web.lower() == website.lower():
               messagebox.showinfo(title=f"{website}", message=f"Username:  {data[web]['username']}\n  Password:  {data[web]['password']}\n")
            else:
               messagebox.showerror(title="404", message=f"No details for the website {website} exists ") 
    finally:
        website_entry.delete(0,END)



def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    website_data = {
         website : {
              "username":username,
              "password":password
         }
    }
    if len(website)==0 and len(password) == 0 :
        messagebox.showerror(title="Oops", message="Website or Username field cannot be empty.")
    else:
            try: 
                with open("password-manager-start\\data.json","r") as password_data:
                    data=json.load(password_data)
                    data.update(website_data)
            except json.decoder.JSONDecodeError:      
                with open("password-manager-start\\data.json","w") as password_data:
                    json.dump(website_data,password_data)
            except FileNotFoundError:      
                with open("password-manager-start\\data.json","w") as password_data:
                    json.dump(website_data,password_data)
            else:        
                with open("password-manager-start\\data.json","w") as password_data:
                    json.dump(data,password_data,indent=4)     

        
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
password_entry.grid(column=1,row=3 , columnspan=2)

generate_button_label = Button(text="Search",command=find_password)
generate_button_label.grid(column=3,row=1)

generate_button_label = Button(text="Generate Password",command=generate_password)
generate_button_label.grid(column=2,row=3,columnspan=2)
 
add_button_label = Button(width=36,text="Add",command=save)
add_button_label.grid(column=0,row=4,columnspan=4)

window.mainloop()