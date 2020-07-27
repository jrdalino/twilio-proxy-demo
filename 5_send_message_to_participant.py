from twilio.rest import Client
from config import ACCOUNT_SID, AUTH_TOKEN


account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN
client = Client(account_sid, auth_token)

message_interaction = client.proxy \
    .services('KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
    .sessions('KCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
    .participants('KPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
    .message_interactions \
    .create(body='Reply to this message to chat!')

print(message_interaction.sid)