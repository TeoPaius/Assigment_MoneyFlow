FROM python:3.7.3
ENV PYTHONBUFFERED 1
ARG ISTEST=0

RUN apt-get update && apt-get install -y gettext postgresql-client

COPY ./requirements /requirements
RUN /bin/bash -c 'if [ $ISTEST == "1" ]; then pip install -r /requirements/test.txt; else pip install -r /requirements/local.txt; fi'

COPY ./compose/local/django/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY ./compose/local/django/start.sh /start.sh
RUN chmod +x /start.sh

COPY ./compose/local/django/celery/worker/start /start-celeryworker
RUN chmod +x /start-celeryworker

RUN mkdir /code
WORKDIR /code
ADD ./code /code

ENTRYPOINT ["/entrypoint.sh"]
