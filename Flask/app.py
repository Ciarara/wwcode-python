from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
	return 'Hello, World!!! This is my first Flask app. 07192020'