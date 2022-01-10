FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /automatica

WORKDIR /automatica

COPY requirements.txt /automatica/

RUN pip install --upgrade pip && pip install -r requirements.txt

ADD . /automatica/
