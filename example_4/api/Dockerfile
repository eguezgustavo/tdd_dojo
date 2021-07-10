FROM python:3.8.5-slim-buster

RUN mkdir /opt/code
RUN mkdir /opt/requirements
WORKDIR /opt/code

ADD requirements /opt/requirements
RUN pip install -r /opt/requirements/development.txt
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]