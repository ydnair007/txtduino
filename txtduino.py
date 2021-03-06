import settings
import sys

from twilio import TwilioRestException
from twilio.rest import TwilioRestClient

try:
    client = TwilioRestClient(settings.twilio_account_sid,
                          settings.twilio_auth_token)
    message = client.sms.messages.create(
        body="File Downloaded and Uploaded to Gdrive!",
        to=settings.your_phone_number,
        from_=settings.your_twilio_number)

except TwilioRestException as e:
    print("Ruh-roh got an error:")

