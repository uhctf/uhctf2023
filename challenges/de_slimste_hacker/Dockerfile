FROM alpine:latest
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

RUN apk add python3
ADD ./src/questions.json /questions.json
ADD ./src/server.py /server.py

ENV THRESHOLD 1000000000
ENV FLAG "uhctf{d1d_y0u-r3al1y_jU5t-8e4t-tH3_5T19?!1}"
EXPOSE 8000
ENTRYPOINT ["/usr/bin/python3"]
CMD ["/server.py", "8000"]