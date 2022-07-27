from ast import Break
from curses import window
from hmac import new
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from xml.etree.ElementTree import indent
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator(): 
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
#take the input and save them to a file and format them and finally clear the entry but before saving we would want to ask the user for confirmation
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    newData = {
        website:{
            "Email": email,
            "Password":password
        }
    }

    
    if not website or not email or not password:
        messagebox.showinfo(title="Please enter your details", message="empty fields")
        return
    
    
    try:
        with open('password.json', 'r') as f:
            data = json.load(f)# read the old data
            data.update(newData)# update the old data
    except FileNotFoundError:
        with open('password.json', 'w') as f:
            json.dump(newData, f, indent=4)
    else:
        with open('password.json', 'w') as f:
            json.dump(data,f,indent=4)# save the updated data
    finally:
        website_entry.delete(0, 'end')
        password_entry.delete(0, 'end')

def search():
    website = website_entry.get()
    with open('password.json', 'r') as f:
        try:
            data = json.load(f)
            Email = data[website]['Email']
            Password = data[website]['Password']
            messagebox.showinfo(title="Your email and password is", message=f"Email: {Email} password: {Password}")
        except KeyError as e:
            messagebox.showinfo(title="Your email and password is", message=f"{e} is not found")
    

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manger")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logoImg = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logoImg)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=18)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "a.abdo.mae@gmail.com")
password_entry = Entry(width=18)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generator)
generate_password_button.grid(row=3, column=2)
Search_password_button = Button(text="Search Password", command=search)
Search_password_button.grid(row=1, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()