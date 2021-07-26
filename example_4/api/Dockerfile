FROM python:3.8.5

RUN mkdir /opt/src
WORKDIR /opt/src

ADD development.txt .
RUN pip3.8 install -r /opt/src/development.txt --no-cache-dir 
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]
