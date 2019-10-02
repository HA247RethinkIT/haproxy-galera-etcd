FROM python:2.7

RUN apt-get update
RUN apt-get install -y haproxy

WORKDIR /app
ADD . /app

# execute everyone's favorite pip command, pip install -r
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install .

ENTRYPOINT ['start.sh']
