FROM alpine:latest
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

RUN apk add python3
RUN apk add py3-pip
RUN apk add build-base
RUN pip3 install pycryptodome
ADD ./src/questions.json /questions.json
ADD ./src/server.py /server.py

ENV THRESHOLD 1000000000
ENV FLAG "uhctf{tH4T_wA5-S0-n0t_cO01-fR0m_Th3_5t195_CryPt0-c0u51n}"
EXPOSE 8001
ENTRYPOINT ["/usr/bin/python3"]
CMD ["/server.py", "8001"]