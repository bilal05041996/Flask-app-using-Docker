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

# 🚀 Publish Docker Image to Docker Hub

This section explains how to **push your local Docker image** to Docker Hub, so you can share it with others or deploy it anywhere.

---

## 🔑 Prerequisites

- A free account on [Docker Hub](https://hub.docker.com/)
- Docker installed locally
- Your Docker image already built (see previous steps)

---

## 🛠 Steps to Push Your Image

### 1. Log in to Docker Hub from terminal

docker login

Enter your Docker Hub username and password when prompted.

2. Check your local images

docker images

3. Tag your image with your Docker Hub username
Replace yourusername with your actual Docker Hub username.

docker tag flask-docker-app yourusername/flask-docker-app

4. Push the tagged image to Docker Hub

docker push yourusername/flask-docker-app

5. Verify your image on Docker Hub
Go to:

https://hub.docker.com/repository/docker/yourusername/flask-docker-app

You should see your uploaded image listed with its tags.

🔄 How to Use Your Published Image
Others (or you) can now pull and run your image anywhere with:

docker pull yourusername/flask-docker-app
docker run -p 5000:5000 yourusername/flask-docker-app

