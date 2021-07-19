FROM python:3.8.5

RUN mkdir /opt/src
RUN mkdir /opt/requirements
WORKDIR /opt/src

ADD requirements /opt/requirements
RUN pip3.8 install -r /opt/requirements/development.txt --no-cache-dir 
    # apk add --no-cache postgresql-libs libffi-dev && \
    # apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    # pip install -r /opt/requirements/development.txt --no-cache-dir &&\
    # apk --purge del .build-deps
COPY . .
ENV PYTHONPATH=":/opt/src"
RUN echo $PYTHONPATH
CMD ["flask", "run", "--host", "0.0.0.0"]