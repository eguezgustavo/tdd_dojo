#!bin/sh

echo {\"apiUrl\": \"${API_URL}\"} > /usr/src/app/src/assets/config.json

npm start