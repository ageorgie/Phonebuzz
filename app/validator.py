from twilio.util import RequestValidator
import os

AUTH_TOKEN = ''

if AUTH_TOKEN == '':
  AUTH_TOKEN = os.environ['TWILIO_TOKEN']

validator = RequestValidator(AUTH_TOKEN)

def isValid(url, signature, postVars = {}):
  return validator.validate(url, postVars, signature)
