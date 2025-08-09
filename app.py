from flask import Flask
import os

app = Flask(__name__)

LOG_FILE = "/app/logs/access.log"

@app.route('/')
def home():
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)  # Ensure directory exists
    with open(LOG_FILE, "a") as f:
        f.write("Home route accessed\n")
    return "Hello! Log recorded."

@app.route('/about')
def about():
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write("About route accessed\n")
    return "About Page"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
