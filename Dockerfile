FROM python:3.7
ENV PYTHONUNBUFFERED 1

# Creating working directory inside container
RUN mkdir /DictionaryDjango
COPY ./DictionaryDjango/. /DictionaryDjango

WORKDIR /DictionaryDjango
RUN pip install -r requirements.txt