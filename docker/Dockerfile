FROM ubuntu:18.04

# Install aws

RUN apt-get update -y \
  && apt-get install -y unzip curl python3.7 python3-pip

ENV LC_ALL=C.UTF-8

ADD requirements.txt .
RUN pip3 install -r requirements.txt

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
  && unzip awscliv2.zip \
  && ./aws/install \
  && rm awscliv2.zip
