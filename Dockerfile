FROM python:alpine3.16

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt 

COPY ./app ./opt/app

WORKDIR /opt/app


CMD ["python3", "main.py"]


