import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    MESSAGE = os.environ.get('WELCOME_MSG', 'Default message')
    return MESSAGE

@app.route('/about')
def about():
    return "This is a simple Flask app running inside a Docker container."

@app.route('/status')
def status():
    return "Status: App is running fine."

@app.route('/log')
def log_route():
    with open("access.log", "a") as f:
        f.write("User visited /log route\n")
    return "Log recorded!"

if __name__ == '__main__':
    # Run Flask on 0.0.0.0 so it's accessible from outside container
    app.run(host='0.0.0.0', port=5000)

