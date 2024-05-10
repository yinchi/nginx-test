FROM python:3-slim
RUN apt update && apt upgrade -y
RUN pip install --no-cache-dir flask
ENV FLASK_APP=hello.py
WORKDIR /app
CMD flask run --host=0.0.0.0
