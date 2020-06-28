#! python3
# text_myself.py - Defines the textmyself() function that texts a message passed to it as a string.

from twilio.rest import Client

# Preset values:
account_sid = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
my_number = '+___________'
twilio_number = '+___________'


def text_myself(message):
    twilio_cli = Client(account_sid, auth_token)
    twilio_cli.messages.create(body=message, from_=twilio_number, to=my_number)