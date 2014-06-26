from app import app
from app import fizzbuzz
from twilio import twiml
from flask import request

@app.route('/')
@app.route('/index')
def index():
  return "Welcome to the PhoneBuzz Test!"

@app.route('/phase1', methods=['GET', 'POST'])
def phase1():
  resp = twiml.Response()
  with resp.gather(action="/fizzbuzz") as g:
    g.say("Please enter a number followed by the pound symbol")

  return str(resp)

@app.route('/fizzbuzz', methods=['GET', 'POST'])
def fizzbuzz_req():
  num = request.form['Digits']
  result = fizzbuzz.fizzbuzz(int(num))
  resp = twiml.Response()
  resp.say(result)

  return str(resp)
  
