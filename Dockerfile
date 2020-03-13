FROM ubuntu:18.04

RUN apt update && apt install -y curl ca-certificates
RUN apt update && apt install -y postgresql
RUN apt update && apt install -y python3 python3-pip\
    libpq-dev\
    python-dev\
    gnupg\
    sudo

RUN curl https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

RUN python3 -m pip install --upgrade --force pip

# Copying requirements seperately so that it can use the cached version while testing
COPY ./Stocks/requirements.txt /Stocks/requirements.txt
RUN pip install -r /Stocks/requirements.txt

COPY ./Stocks /Stocks




