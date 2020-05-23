FROM python:3.8.3-slim

ENV PYTHONUNBUFFERED 1
ENV FLASK_APP=store.py FLASK_RUN_PORT=8000

WORKDIR /app

COPY requirements.txt ${WORKDIR}
COPY store.py ${WORKDIR}

RUN pip install -r requirements.txt

ENTRYPOINT [ "flask", "run", "--host=0.0.0.0" ]

EXPOSE ${FLASK_RUN_PORT}
