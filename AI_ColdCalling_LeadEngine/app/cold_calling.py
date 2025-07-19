from app.utils import generate_call_script
from twilio.rest import Client
import os

account_sid = os.getenv('TWILIO_SID')
auth_token = os.getenv('TWILIO_AUTH')
twilio_number = os.getenv('TWILIO_PHONE')

def make_cold_call(phone_number, lead_info):
    client = Client(account_sid, auth_token)
    script = generate_call_script(lead_info)

    try:
        call = client.calls.create(
            twiml=f'<Response><Say>{script}</Say></Response>',
            to=phone_number,
            from_=twilio_number
        )
        return 'Call initiated'
    except Exception as e:
        return f'Error: {str(e)}'
