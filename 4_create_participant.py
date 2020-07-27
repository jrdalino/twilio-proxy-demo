from twilio.rest import Client
from config import ACCOUNT_SID, AUTH_TOKEN, SERVICE_ID, SESSION_ID

account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN
service_id = SERVICE_ID
session_id = SESSION_ID
client = Client(account_sid, auth_token)

participant_1 = client.proxy \
                    .services(service_id) \
                    .sessions(session_id) \
                    .participants \
                    .create(friendly_name='Driver', identifier='+6512345678')

print(participant_1.proxy_identifier)

participant_2 = client.proxy \
                    .services(service_id) \
                    .sessions(session_id) \
                    .participants \
                    .create(friendly_name='Rider', identifier='+6512345679')

print(participant_2.proxy_identifier)