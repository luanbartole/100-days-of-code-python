from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

EMAIL = "email@gmail.com"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.delete(0, "end")
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_text = website_entry.get()
    login_text = login_entry.get()
    pass_text = pass_entry.get()
    final_text = f"{web_text} | {login_text} | {pass_text}\n"

    if len(web_text) == 0 or len(login_text) == 0 or len(pass_text) == 0:
        messagebox.showinfo(title="Warning", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=web_text,
                                       message=f"Details entered were as follows: \nEmail: {login_text} \nPassword:{pass_text} \nSave data?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(final_text)
                website_entry.delete(0, "end")
                pass_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager by Luan Bartole")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(column=0, row=0, columnspan=3)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=59)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
website_entry.focus()

login_label = Label(text="Email/Username:")
login_label.grid(column=0, row=2)
login_entry = Entry(width=59)
login_entry.grid(column=1, row=2, columnspan=2, sticky="w")
login_entry.insert(0, EMAIL)

pass_label = Label(text="Password")
pass_label.grid(column=0, row=3)
pass_entry = Entry(width=40)
pass_entry.grid(column=1, row=3, sticky="w")

genpass_button = Button(text="Generate Password", command=generate_password)
genpass_button.grid(column=2, row=3, sticky="w")
addpass_button = Button(text="Add", width=50, command=save)
addpass_button.grid(column=1, row=4, columnspan=2, sticky="w")

window.mainloop()
