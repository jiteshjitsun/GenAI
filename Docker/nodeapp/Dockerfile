# Base image
FROM node:20.17.0-alpine3.19

WORKDIR /home/app/

# RUN apt-get update && apt-get install -y curl
# RUN curl -sL https://deb.nodesource.com/setup_22.x -o /tmp/nodesource_setup.sh
# RUN bash /tmp/nodesource_setup.sh
# RUN apt install -y nodejs

# Copying source code to docker image
# COPY package-lock.json package-lock.json
# COPY package.json package.json

COPY package*.json .

RUN npm install

COPY app.js app.js

EXPOSE 8000


CMD [ "npm", "start" ]
