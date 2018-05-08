FROM ubuntu
MAINTAINER Aidan Holland

EXPOSE 3000

RUN apt-get update
RUN apt-get install -y build-essential python3 python3-pip

RUN pip install -r requirements.txt

CMD python app.py
