from app import app
from twilio import twiml

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
def fizzbuzz():
  num = @app.request.args.get('Digits')
  
  result = fizzbuzz(num)
  
  resp = twiml.Response()
  resp.say(result)

  return str(resp)
  
