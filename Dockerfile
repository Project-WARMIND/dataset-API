FROM python:3.6.5
MAINTAINER Aidan Holland

COPY . .
RUN pip install -r ./requirements.txt

CMD python app.py
