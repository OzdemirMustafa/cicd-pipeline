FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt ./requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /src
WORKDIR /src
COPY ./src /src

RUN adduser -D user
USER user

EXPOSE 8000
CMD ["python", "serve.py"]