# 🚀 Dockerized Flask Web Application

This is a simple Python web application built with Flask and containerized using Docker. It demonstrates how to create, build, and run a containerized Flask application.

---

## 📁 Project Structure

docker-flask-app/
├── app.py # Main Flask web server code
├── requirements.txt # Python dependencies
└── Dockerfile # Dockerfile to build the image


---

## 📦 Technologies Used

- Python 3.9
- Flask 2.3
- Docker

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/docker-flask-app.git
cd docker-flask-app

2. Build the Docker image

docker build -t flask-docker-app .

3. Run the Docker container
docker run -d -p 5000:5000 flask-docker-app

4. Open in browser
Navigate to: http://localhost:5000
You should see:

Hello from Dockerized Flask App!

******
Here, for docker compose concept just refer app.py and I have done changes

---app.py---
Here, os.environ.get('WELCOME_MSG', 'Default message')
means if WELCOME_MSG is not set, it will show "Default message".

This is important because now Docker Compose can pass that variable.

Your project folder should have:

docker-flask-app/
├── app.py
├── requirements.txt
├── Dockerfile
└── docker-compose.yml

Build & start with Docker Compose
From inside the folder where docker-compose.yml is located:

docker-compose up --build
--build ensures it rebuilds the image with the latest changes.

This will start the container and show logs in your terminal.

Access your app in your browser

Stop the container using

docker-compose down

If you want the container to run in the background:
docker-compose up -d --build

Then check logs anytime:
docker-compose logs -f <service_name>

Here, -f means show the logs until I press Ctrl C
******

******

What you should edit in your previous code
Your current app.py already has /, /about, /status routes.
You can add this new /log route to track visits.
Here’s your updated app.py:

@app.route('/log')
def log_route():
    with open("access.log", "a") as f:
        f.write("User visited /log route\n")
    return "Log recorded!"

Check the log inside the container:

docker exec -it <container_id> cat access.log

******

******
Bind Volumes (Access logs on your host):
volumes: →
./logs is the folder on your host (relative to docker-compose.yml).
/app/logs is the folder inside the container where the Flask app writes logs.

This means anything your app writes to /app/logs will instantly be available in ./logs on your host.

*****

*****
# 🐳 Flask App with Docker Volume Binding (Logs on Host)

This project demonstrates how to **bind mount a volume** in Docker so that logs generated inside a container are stored on your **host machine**.

---

## 📂 Project Structure
docker-flask-app/
├── app.py # Flask application
├── requirements.txt # Python dependencies
├── Dockerfile # Image build instructions
├── docker-compose.yml # Compose config with volume bind
└── logs/ # Logs will be saved here (created automatically)

## ⚙️ How It Works

- Flask app writes logs to `/app/logs/access.log` inside the container.
- Docker Compose binds the **host folder** `./logs` to `/app/logs` inside the container.
- Any file created in `/app/logs` inside the container appears in the host's `logs` folder.

*****
