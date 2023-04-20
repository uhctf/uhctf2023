#! /bin/bash

echo 'http --lport 8080 --lhost 127.0.0.1 --persistent --website reddid.com' | /root/sliver-server
/usr/sbin/apachectl -D FOREGROUND