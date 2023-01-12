from twilio.rest import Client
import smtplib
import os

BOT_EMAIl = os.environ.get("PYTHON_EMAIL")
BOT_PASSWORD = os.environ.get("PYTHON_EMAIL_PASSWORD")


class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""

    def __init__(self, twilio_sid, twilio_token, twilio_phone_a, twilio_phone_b):
        self.account_sid = twilio_sid
        self.auth_token = twilio_token
        self.phone_a = twilio_phone_a
        self.phone_b = twilio_phone_b

    def send_sms(self, text: str):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body=text,
            from_=self.phone_a,
            to=self.phone_b
        )
        print(message.status)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(BOT_EMAIl, BOT_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=BOT_EMAIl,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
