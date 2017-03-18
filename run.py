# Imports the app variable from our app package 
# and invokes its run method to start the server. 
# (the app variable holds the Flask instance)

from webapp import app
app.run(debug=True)