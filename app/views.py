from app import app
from twilio import twiml

@app.route('/')
@app.route('/index')
def index():
  return "Welcome to the PhoneBuzz Test!"

@app.route('/phase1', methods=['GET', 'POST'])
def phase1():
  resp = twiml.Response()
  resp.say('Hey welcome to PhoneBuzz')

  return str(resp)
  
