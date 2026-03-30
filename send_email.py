import smtplib
from config import *

def send_email(to, msg):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(EMAIL, EMAIL_PASSWORD)
    server.sendmail(EMAIL, to, msg)
    server.quit()
