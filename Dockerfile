FROM python:3.9

WORKDIR /app

COPY ./requirements-dev.txt requirements-dev.txt
COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt -r requirements-dev.txt

COPY ./src src
COPY ./app.py app.py

CMD ["python", "app.py"]
