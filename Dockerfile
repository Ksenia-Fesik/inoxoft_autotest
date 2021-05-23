FROM jenkins/jenkins:lts-jdk11
USER root
RUN mkdir /my_app
WORKDIR /my_app
COPY requirements.txt /my_app
RUN pwd
RUN ls -la
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
RUN echo "deb https://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update
RUN apt-get install -y python3-pip libnss3 google-chrome-stable
