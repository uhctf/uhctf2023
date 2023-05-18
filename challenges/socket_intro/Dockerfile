FROM alpine:3.17

RUN apk add --no-cache socat python3
ADD server.py server.py
EXPOSE 8000

CMD socat tcp-l:8000,reuseaddr,fork system:'python server.py'