FROM python:3.10

RUN apt-get update

WORKDIR /app

COPY app.py app.py
COPY predictor.py predictor.py
COPY iris_model.pkl iris_model.pkl
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD python app.py