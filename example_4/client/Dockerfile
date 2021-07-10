# Client App
FROM node:12-alpine
WORKDIR /usr/src/app
COPY ["package.json", "npm-shrinkwrap.json*", "./"]
RUN npm install --silent
COPY . .
CMD ["npm", "start"]
