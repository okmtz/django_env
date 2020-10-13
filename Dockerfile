FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /django_env
ADD requirements.txt /django_env/
RUN pip install -r requirements.txt
RUN pip install django-environ
ADD . /django_env/
