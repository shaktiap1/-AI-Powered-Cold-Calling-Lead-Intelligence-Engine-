import os
from twilio.rest import Client

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
TWILIO_AUTH_TOKEN  = os.getenv("TWILIO_AUTH_TOKEN", "your_auth_token")
TWILIO_PHONE       = os.getenv("TWILIO_PHONE_NUMBER", "+1234567890")
BASE_URL           = os.getenv("EXTERNAL_BASE_URL", "https://your-ngrok-domain.ngrok.io")  # For webhooks

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def make_call(to_number: str, lead_id: str) -> str:
    """Initiate an outbound voice call to the given number, returning Twilio Call SID."""
    call = client.calls.create(
        to=to_number,
        from_=TWILIO_PHONE,
        url=f"{BASE_URL}/api/call/voice?lead_id={lead_id}",
        status_callback=f"{BASE_URL}/api/call/status",
        status_callback_event=["initiated", "ringing", "answered", "completed"],
        record=True
    )
    return call.sid
