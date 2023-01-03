import pandas
import random
import smtplib
import datetime as dt

data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")
current = dt.datetime.now()
# Used to hide the email credentials from the demo video
for _ in range(1):
    user_email = "email@gmail.com"
    user_password = "password"


def birthday_letter(name, email):
    """Pick a random letter template and make a custom birthday letter."""
    # Creates the custom letter
    letter_number = random.randint(1, 3)
    with open(file=f"letter_templates/letter_{letter_number}.txt") as birthday_template:
        custom_letter = birthday_template.readlines()
        custom_letter[0] = custom_letter[0].replace("[NAME]", f"{name}")
        final_letter = "".join(custom_letter)

    # Sends the custom letter
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user_email, user_password)
        connection.sendmail(
            from_addr=user_email,
            to_addrs=email,
            msg=f"Subject: Happy Birthday {name} \n\n{final_letter}"
        )


for person in data_dict:
    if current.day == person["day"] and current.month == person["month"]:
        birthday_letter(name=person["name"], email=person["email"])
