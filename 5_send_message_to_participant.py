from twilio.rest import Client
from config import ACCOUNT_SID, AUTH_TOKEN, SERVICE_ID, SESSION_ID, PARTICIPANT_ID


account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN
service_id = SERVICE_ID
session_id = SESSION_ID
participant_id = PARTICIPANT_ID 
client = Client(account_sid, auth_token)

message_interaction = client.proxy \
    .services(service_id) \
    .sessions(session_id) \
    .participants(participant_id) \
    .message_interactions \
    .create(body='Reply to this message to chat!')

print(message_interaction.sid)