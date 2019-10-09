FROM python:2.7-slim

RUN apt-get update
RUN apt-get install -y haproxy

# reset apt-mark's "manual" list so that "purge --auto-remove" will remove all build dependencies
RUN apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false; \
rm -rf /var/lib/apt/lists/*

WORKDIR /app
ADD . /app

# execute everyone's favorite pip command, pip install -r
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install .

CMD ["/usr/local/bin/haproxy-etcd"]
