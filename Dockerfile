FROM python:3-alpine3.7
WORKDIR /app/src
COPY ./ ./
RUN pip install --upgrade pip && \
    pip install -r requirements.txt