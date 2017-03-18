# start the server - 
# imports the app variable from the webapp subdirectory (package) 
# and invokes its run method to start the server (app is an instance of Flask)

from webapp import app
app.run(debug=True)