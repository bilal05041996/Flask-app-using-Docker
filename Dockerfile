FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirement.txt

EXPOSE 5000

ENV WELCOME_MSG="Hello from Default docker Build"

CMD ["python", "app.py"]

