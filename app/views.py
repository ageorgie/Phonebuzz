from app import app
from app import fizzbuzz
from app import validator
from app import twilio_client
from twilio import twiml
from flask import request
from flask import render_template
import time

history = []
callRequests = {}

@app.before_request
def before_request():
  if request.path in ["/phase1", "/fizzbuzz"]:
    if (not validator.isValid(request.url, request.headers['X-Twilio-Signature'], request.form)):
      return "That is invalid"

@app.route('/')
@app.route('/index')
def index():
  global history
  global callRequests
  return render_template("index.html", history=history, callRequests=callRequests)

@app.route('/phase1', methods=['POST'])
def phase1():
  currentTime = request.args.get('time') or ""
  resp = twiml.Response()
  with resp.gather(action=("/fizzbuzz?time="+currentTime)) as g:
    g.say("Please enter a number followed by the pound symbol")

  return str(resp)

@app.route('/fizzbuzz', methods=['POST'])
def fizzbuzz_req():
  global callRequests

  num = request.form['Digits']
  currentTime = request.args.get('time')
  
  if currentTime in callRequests:
    callRequests[currentTime] += (num,)
  
  result = fizzbuzz.fizzbuzz(int(num))
  
  resp = twiml.Response()
  resp.say(result)

  return str(resp)

@app.route('/replay', methods=['POST'])
def replay():
  num = request.form['Digits']
  phoneNum = request.form['Phone']

  print request.url_root+"phase1"
  twilio_client.client.calls.create(to=phoneNum, from_="4378000684", url=request.url_root+"phase1", send_digits=num)

  return "The call will start momentarily"



@app.route('/start_outgoing_call', methods=['POST'])
def start_outgoing_call():
  global history
  global callRequests

  num = request.form['phone']
  delay = request.form['delay']
  
  currentTime = time.strftime('%d.%m.%Y%I.%M.%S')
  
  history.append(currentTime)
  callRequests[currentTime] = (delay, num)
  
  time.sleep(int(delay))
  
  twilio_client.client.calls.create(to=num, from_="4378000684", url=request.url_root+"phase1?time="+currentTime)
  
  return "The call will start momentarily"

