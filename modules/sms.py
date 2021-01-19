from twilio.rest import Client

class SMS:
    def __init__(self, account_sid: str, auth_token: str, phone_to: str, phone_from: str):
        self.phone_to = phone_to
        self.phone_from = phone_from
        self.client = Client(account_sid, auth_token)

    def send_alert(self, msg: str):
        self.client.api.account.messages.create(
            to=self.phone_to,
            from_=self.phone_from,
            body=msg
        )
