from twilio.rest import Client
from config import ACCOUNT_SID, AUTH_TOKEN, SERVICE_ID

account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN
service_id = SERVICE_ID
client = Client(account_sid, auth_token)

session = client.proxy.services(service_id) \
                      .sessions \
                      .create(unique_name='MyFirstSession')

print(session.sid)