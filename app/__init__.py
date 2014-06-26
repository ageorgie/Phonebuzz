from flask import Flask

app = Flask(__name__)

from app import views
from app import twilio_client

twilio_client = twilio_client.client
