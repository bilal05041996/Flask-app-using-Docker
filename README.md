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
