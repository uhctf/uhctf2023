FROM ubuntu:kinetic

# gonna compile for 32bit
RUN dpkg --add-architecture i386
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y libssl-dev:i386
RUN apt-get install -y libc6-dev:i386
RUN apt-get install -y clang:i386
RUN apt-get install -y gcc:i386
RUN apt-get clean

COPY ./src/ /app/src/

WORKDIR /app/src/
RUN ./build.sh

# run website
WORKDIR /app/src/website
EXPOSE 80
CMD gunicorn --bind 0.0.0.0:80 wsgi:app