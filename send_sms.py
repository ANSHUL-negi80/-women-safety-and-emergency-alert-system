from twilio.rest import Client
from config import *

def send_sms(phone, msg):
    client = Client(TWILIO_SID, TWILIO_TOKEN)
    client.messages.create(body=msg, from_=TWILIO_PHONE, to=phone)
