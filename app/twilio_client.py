from twilio.rest import TwilioRestClient
import os

account = "avav"
token = "aevae"

if(account == "" or token == ""):
  account = os.environ['TWILIO_ACCOUNT']
  token = os.environ['TWILIO_TOKEN']

client = TwilioRestClient(account, token)
  