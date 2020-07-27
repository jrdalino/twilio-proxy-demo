# Twilio Proxy Demo

## Requirements
- a Twilio account – sign up for free
- Python 2.x or 3.x
- the Twilio Python helper library

## Environment and project setup
- Sign up for Twilio, Purchase two Twilio Phone Number and Note Account SID, Auth Token & Phone Number SID

- Install and activate virtualenv
```
python3 -m venv venv
source venv/bin/activate
```

- Create requirements.txt
```
twilio
```

- Installs dependencies
```
pip install -r requirements.txt
```

## Create Python App
- Create app.py
```
from twilio.rest import Client
from config import ACCOUNT_SID, AUTH_TOKEN


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
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
```

- Run your application
```
$ cd ~/environment/twilio-proxy-demo
$ python3 1_create_service.py
$ python3 2_add_phone_number.py
$ python3 3_create_session.py
$ python3 4_create_participant.py
$ python3 5_send_message_to_participant.py
```

## References
- https://www.twilio.com/docs/proxy
- https://www.twilio.com/docs/proxy/quickstart