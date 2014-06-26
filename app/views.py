from app import app
from app import fizzbuzz
from app import validator
from twilio import twiml
from flask import request

@app.before_request
def before_request():
  if request.path in ["/phase1", "/fizzbuzz"]:
    if (not validator.isValid(request.url, request.headers['X-Twilio-Signature'], request.form)):
      return "That is invalid"

@app.route('/')
@app.route('/index')
def index():
  return render_template("index.html")

@app.route('/phase1', methods=['POST'])
def phase1():
  resp = twiml.Response()
  with resp.gather(action="/fizzbuzz") as g:
    g.say("Please enter a number followed by the pound symbol")

  return str(resp)

@app.route('/fizzbuzz', methods=['POST'])
def fizzbuzz_req():
  num = request.form['Digits']
  result = fizzbuzz.fizzbuzz(int(num))
  resp = twiml.Response()
  resp.say(result)

  return str(resp)
  
