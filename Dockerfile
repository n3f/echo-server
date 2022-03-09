FROM alpine

RUN apk add --no-cache --update python3

COPY serve.py /

ENTRYPOINT ["python3", "/serve.py"]