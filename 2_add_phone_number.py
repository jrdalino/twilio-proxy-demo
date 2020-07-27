from twilio.rest import Client
from config import ACCOUNT_SID, AUTH_TOKEN

account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN
client = Client(account_sid, auth_token)

phone_number = client.proxy \
                     .services('KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                     .phone_numbers \
                     .create(sid='PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

print(phone_number.sid)