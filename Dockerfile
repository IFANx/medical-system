FROM python:3.7

WORKDIR /usr/src/medical

COPY ./.pip /root/.pip
COPY ./app ./app
COPY ./setup.py ./setup.py
COPY run.py run.py
COPY ./instance ./instance
COPY MANIFEST MANIFEST
COPY uwsgi.ini uwsgi.ini

RUN pip install -e .
ENV FLASK_ENV=poduction FLASK_APP=app

CMD ["uwsgi", "--ini", "uwsgi.ini"]
