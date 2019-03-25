FROM nginx:alpine as nginx
COPY ./conf/nginx.conf /etc/nginx/nginx.conf
COPY ./static /static

FROM python:3-alpine3.7 as app
WORKDIR /app/src
COPY ./ ./
# Static will be copied to nginx image
RUN rm -r static
ENV PIP_CACHE_DIR=/app/pip-cache
RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && rm -rf /app/pip-cache/*
