# create a Flask object
from flask import Flask
app = Flask(__name__)

# and import the views module
from webapp import views
# import comes at the end (because views needs app)