FROM ubuntu:18.04

# Install aws

RUN apt update -y \
  && apt install -y unzip curl python3-pip

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
  && unzip awscliv2.zip \
  && ./aws/install \
  && rm awscliv2.zip
