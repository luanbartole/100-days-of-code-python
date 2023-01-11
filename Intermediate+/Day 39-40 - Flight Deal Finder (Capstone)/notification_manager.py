from twilio.rest import Client


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
