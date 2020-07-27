from twilio.rest import Client
from config import ACCOUNT_SID, AUTH_TOKEN

account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN
client = Client(account_sid, auth_token)

session = client.proxy.services('KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                      .sessions \
                      .create(unique_name='MyFirstSession')

print(session.sid)