from tkinter import *

FONT = ("Arial", 12)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)

entry = Entry(width=10, textvariable="a")
entry.insert(END, string="0")
# print(entry.get())
entry.grid(column=1, row=0)

label0 = Label(text="Miles", font=FONT)
label0.grid(column=2, row=0)

label1 = Label(text="Is equal to", font=FONT)
label1.grid(column=0, row=1)

label2 = Label(text="0", font=FONT)
label2.grid(column=1, row=1)

label3 = Label(text="Km", font=FONT)
label3.grid(column=2, row=1)


def action():
    label2["text"] = round(int(entry.get()) * 1.609344, 1)


# calls action() when pressed
button = Button(text="Convert", command=action)
button.grid(column=1, row=2)

window.mainloop()
