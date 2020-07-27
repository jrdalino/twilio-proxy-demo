from twilio.rest import Client
from config import ACCOUNT_SID, AUTH_TOKEN

account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN
client = Client(account_sid, auth_token)

participant = client.proxy \
                    .services('KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                    .sessions('KCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                    .participants \
                    .create(friendly_name='Alice', identifier='+15558675310')

print(participant.proxy_identifier)