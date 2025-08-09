import os
from flask import Flask

app = Flask(__name__)

# Read environment variable, set default if not provided
MESSAGE = os.getenv("WELCOME_MSG", "Hello from Dockerized Flask App!")

@app.route('/')
def home():
    return MESSAGE

@app.route('/about')
def about():
    return "This is a simple Flask app running inside a Docker container."

@app.route('/status')
def status():
    return "Status: App is running fine."

if __name__ == '__main__':
    # Run Flask on 0.0.0.0 so it's accessible from outside container
    app.run(host='0.0.0.0', port=5000)

