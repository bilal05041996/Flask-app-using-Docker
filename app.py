from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Dockerized Flask App!"

#Route: About
@app.route('/about')
def about():
    return "This is a simple flask app running inside a Docker container"
#Route: Status
@app.route('/status')
def status():
    return "Status: App is running fine"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

