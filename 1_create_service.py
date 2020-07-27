from twilio.rest import Client
from config import ACCOUNT_SID, AUTH_TOKEN

account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN
client = Client(account_sid, auth_token)

service = client.proxy.services.create(unique_name='owl_taxis_demo')

print(service.sid)