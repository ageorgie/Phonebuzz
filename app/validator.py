print "START OF VALIDATOR"
from twilio.util import RequestValidator
import os

print "BEFORE AUTH_TOKEN"
AUTH_TOKEN = ''

if AUTH_TOKEN == '':
  AUTH_TOKEN = os.environ['TWILIO_TOKEN']

print "AFTER AUTH_TOKEN"

validator = RequestValidator(AUTH_TOKEN)

print "AFTER VALIDATOR INITIALIZATION"
print validator
def isValid(url, signature, postVars = {}):
  print "I AM HERE"
  return validator.validate(url, postVars, signature)

print "AFTER isValid DECLARATION"