from twilio.rest import TwilioRestClient
import os

account = ""
token = ""

if(account == "" or token == ""):
  account = os.environ['TWILIO_ACCOUNT']
  token = os.environ['TWILIO_TOKEN']

client = TwilioRestClient(account, token)
  