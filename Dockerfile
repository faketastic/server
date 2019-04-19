FROM python:3.6-slim

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential libpq-dev
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "server.py", "--debug"]