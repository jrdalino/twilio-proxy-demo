from twilio.rest import Client
from config import ACCOUNT_SID, AUTH_TOKEN, SERVICE_ID, CA_PHONE_ID, WA_PHONE_ID, SG_PHONE_ID

account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN
service_id = SERVICE_ID
ca_phone_id = CA_PHONE_ID
wa_phone_id = WA_PHONE_ID
sg_phone_id = SG_PHONE_ID

client = Client(account_sid, auth_token)

phone_number_sg = client.proxy \
                     .services(service_id) \
                     .phone_numbers \
                     .create(sid=sg_phone_id)

print(phone_number_sg.sid)

phone_number_wa = client.proxy \
                     .services(service_id) \
                     .phone_numbers \
                     .create(sid=wa_phone_id)

print(phone_number_wa.sid)