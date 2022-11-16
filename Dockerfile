FROM python:3.10
RUN apt-get update -y && apt-get install pip -y

RUN mkdir main
WORKDIR main
RUN pip install virtualenv && virtualenv venv && . venv/bin/activate
COPY ./requirements.txt .
RUN pip install -r requirements.txt
CMD ["main.py"]