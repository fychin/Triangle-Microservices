FROM python:3.8.3-slim

ENV PYTHONUNBUFFERED 1
ENV FLASK_APP=app/store.py FLASK_RUN_PORT=8000

COPY requirements.txt .
COPY config.py .
COPY app/ app/

RUN pip install -r requirements.txt

ENTRYPOINT [ "flask", "run", "--host=0.0.0.0" ]

EXPOSE ${FLASK_RUN_PORT}
