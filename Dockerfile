FROM python:3.6.5-slim

# set the working directory in the container to /app
WORKDIR /app

# add the current directory to the container as /app
ADD . /app

# execute everyone's favorite pip command, pip install -r
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Update software and add dnsutils for network debugging
RUN apt-get update
RUN apt-get install dnsutils -y
