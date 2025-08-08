#This code is used to run the Flask app inside a container

#tells docker to use official Python 3.9 slim image from Docker Hub. slim means a smaller version of full Python image (faster and lighter). It is abase image for your container.
FROM python:3.9-slim

#set working directory inside container to /app. All next command (COPY, RUN, etc.) will be run inside /app.
WORKDIR /app

#copy project files into container means it copy everything from your local project folder into container /app directory.
COPY . .

#install all python required packages listed in requirements.txt
#--no-cache-dir reduces the image size by not caching (storing the data temporarily) files
RUN pip install --no-cache-dir -r requirement.txt

#This documents taht your app listens on port 5000 inside the container. But docker doesn't automatically make that port accessible to your computer or browser.
#export -> doesn't publish or open the port to outside. It does not make your app reachable from browser.
EXPOSE 500

#run the flask app. This is the default comamnd Docker run when container start
CMD ["python","app.py"]

#summary

#Starts from Python 3.9 image

#Copies your Flask project files into container

#Installs required packages

#Prepares to serve the app on port 5000

#Runs your app with python app.py



