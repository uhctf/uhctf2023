FROM ubuntu:18.04

RUN apt-get update && apt-get install -y socat gcc gcc-multilib

# Note: only the contents are copied
COPY ./src/ /
WORKDIR /

RUN gcc -g -fno-stack-protector -m32 /main.c -o /honourable_overwrite

# Add flag
RUN sed 's/puts.*/puts("uhctf{8uff3r-0v3rf10w-70-7h3-k1n9d0m-26fa2b}");/g' -i /main.c
RUN gcc -g -fno-stack-protector -m32 /main.c -o /honourable_overwrite_with_flag

RUN mkdir -p /attachments/
CMD cp /honourable_overwrite /attachments/honourable_overwrite && socat tcp-l:1337,reuseaddr,fork system:'/honourable_overwrite_with_flag'