FROM alpine:3.17

RUN apk add --no-cache socat python3
ADD server.py server.py
EXPOSE 4200

CMD socat tcp-l:4200,reuseaddr,fork system:'python server.py'