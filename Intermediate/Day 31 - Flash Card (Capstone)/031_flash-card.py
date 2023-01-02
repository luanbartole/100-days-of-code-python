import pandas
from tkinter import *
from tkinter import messagebox
from random import choice

# Constants and Variables
BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"
# First run = French Words file / Not first run = Words to Learn file
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    data_dict = data.to_dict(orient="records")

current_card = {}


# ---------------------------- CREATE FLASH CARDS ------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(data_dict)
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


# ---------------------------- SAVE PROGRESS ------------------------------- #
def save_progress():
    global data_dict
    data_dict.remove(current_card)
    # If the user learned all the words, it starts from 0
    if not data_dict:
        new_data = pandas.read_csv("data/french_words.csv")
        data_dict = new_data.to_dict(orient="records")
        messagebox.showinfo(title="Congratulations",
                            message="You learned all the 100 words! \nI'm gonna reset the list now.")

    df = pandas.DataFrame(data_dict)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card by Luan Bartole")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Start the timer to flip the card and show the answer.
flip_timer = window.after(3000, func=flip_card)

# Images
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right_logo = PhotoImage(file="images/right.png")
wrong_logo = PhotoImage(file="images/wrong.png")

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=card_front)
language_text = canvas.create_text(400, 150, text="", font=(FONT, 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=(FONT, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
right_button = Button(image=right_logo, highlightthickness=0, bd=0.1, command=save_progress)
right_button.grid(column=0, row=1)
wrong_button = Button(image=wrong_logo, highlightthickness=0, bd=0.1, command=next_card)
wrong_button.grid(column=1, row=1)

# Changes to a different flash card.
next_card()

window.mainloop()
