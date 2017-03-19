# create a Flask object
from flask import Flask
app = Flask(__name__)

# and import the routes
# (routes is a file in the webapp directory)
from webapp import routes
# this import comes at the end because routes needs to know abut the app object's methods
