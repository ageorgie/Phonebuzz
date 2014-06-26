from app import app
from app import fizzbuzz
from app import validator
from twilio import twiml
from flask import request

@app.route('/')
@app.route('/index')
def index():
  return "Welcome to the PhoneBuzz Test!"

@app.route('/phase1', methods=['POST'])
def phase1():
  print request.url
  print request.headers['X-Twilio-Signature']
  print request.form
  # return if not validator.isValid(request.url, request.headers['X-Twilio-Signature'], request.form)
  resp = twiml.Response()
  with resp.gather(action="/fizzbuzz") as g:
    g.say("Please enter a number followed by the pound symbol")

  return str(resp)

@app.route('/fizzbuzz', methods=['POST'])
def fizzbuzz_req():
  print request.headers
  num = request.form['Digits']
  result = fizzbuzz.fizzbuzz(int(num))
  resp = twiml.Response()
  resp.say(result)

  return str(resp)
  
