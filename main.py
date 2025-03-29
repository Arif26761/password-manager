from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    random_password = "".join(password_list)
    user_password.insert(9, random_password)
    pyperclip.copy(user_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = web_link.get()
    email = email_username.get()
    password = user_password.get()

    if len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Opps", message="Please fill out all the necessary fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \n"
                                                              f"Password: {password} \nIs it ok to save?")
        if is_ok:
            with open("userData.txt", "a") as data_file:  # With statement auto closes the file once the code is run.
                data_file.write(f"{website}  |  {email}  |  {password} \n")

                web_link.delete(0, END)
                user_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("Password Manager")
window.config(padx=50, pady=50)

# canvas image
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Entries
web_link = Entry(width=51)  # for mac width=35
web_link.focus()
email_username = Entry(width=51)  # for mac width=35
email_username.insert(0, "user@gmail.com")
user_password = Entry(width=32)  # for mac width=22
web_link.grid(column=1, row=1, columnspan=2)
email_username.grid(column=1, row=2, columnspan=2)
user_password.grid(column=1, row=3)

# Labels
website_label = Label(text="Website:")
email_label = Label(text="Email/Username:")
password_label = Label(text="Password:")
website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

# Button
add_button = Button(text="Add", width=43, command=save)  # for mac width=36
generate_password_button = Button(text="Generate Password", command=generate_password)
add_button.grid(column=1, row=4, columnspan=2)
generate_password_button.grid(column=2, row=3)

window.mainloop()
