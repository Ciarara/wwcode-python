from flask import Flask #import the Flask class
app = Flask(__name__) #create an instance of the class, used the __name__ for the single module here


@app.route('/') #used the route() decorator to tell Flask what URL should trigger our function.
def hello_world(): #the function is given a name which is also used to generate URLs for that particular function, and returns the message we want to display in the user’s browser.
	return 'Hello, World!!! This is my first Flask app. 07192020'

#NOTE: Just save it as hello.py or something similar. Make sure to not call your application flask.py because this would conflict with Flask itself.

#To run the application you can either use the flask command or python’s -m switch with Flask. Before you can do that you need to tell your terminal the application to work with by exporting the FLASK_APP environment variable:

#$ export FLASK_APP=hello.py
# To run your app in debug mode, set the FLASK_DEBUG environment variable to 1 before running the application:
#$ export FLASK_DEBUG=1
#$ flask run
 #* Running on http://127.0.0.1:5000/
