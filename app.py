from twilio.rest import Client
from config import ACCOUNT_SID, AUTH_TOKEN


account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN
client = Client(account_sid, auth_token)

# Step 1: Create a Service
service = client.proxy.services.create(unique_name='unique_name')

print(service.sid)

# Step 2.a: Add a phone number A to your service
phone_number = client.proxy \
                     .services('KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                     .phone_numbers \
                     .create(sid='PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

print(phone_number.sid)

# Step 2.b: Add a phone number B to your service
phone_number = client.proxy \
                     .services('KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                     .phone_numbers \
                     .create(sid='PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

print(phone_number.sid)

# Step 3: Create a Session
session = client.proxy.services('KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                      .sessions \
                      .create(unique_name='MyFirstSession')

print(session.sid)

# Step 4: Create participants
participant = client.proxy \
                    .services('KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                    .sessions('KCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                    .participants \
                    .create(friendly_name='Alice', identifier='+15558675310')

print(participant.proxy_identifier)

# Step 5: Send a text message
message_interaction = client.proxy \
    .services('KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
    .sessions('KCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
    .participants('KPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
    .message_interactions \
    .create(body='Reply to this message to chat!')

print(message_interaction.sid)

# Step 6: Make a voice call - If your Twilio Phone Numbers are voice capable, you're now ready for a proxied voice conversation