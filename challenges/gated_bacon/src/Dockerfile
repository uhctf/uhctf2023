FROM ubuntu:23.04

RUN apt-get update && apt-get -y upgrade

# systemd replacement (sliver install script uses systemd but containers can't use it)
RUN apt-get install -y python3 curl
RUN curl https://raw.githubusercontent.com/gdraheim/docker-systemctl-replacement/190870f1bbee4d6ba4f1fdfa85da9bcdfc0b44d6/files/docker/systemctl3.py -o /usr/bin/systemctl
RUN chmod +x /usr/bin/systemctl

# setup C2
## Specify release v1.5.34 to make sure the database will work, and skip verification (as it'd error attempting to check the newer version)
RUN curl https://sliver.sh/install | sed 's/latest/91630410/' | sed 's/^gpg.*verify/# gpg/g' | bash
## Sliver needs to know about the pre-generated beacon
ADD ./assets/sliver/sliver.db /root/.sliver/sliver.db

# setup redirector
RUN apt-get install -y apache2
ADD ./assets/apache/000-default.conf /etc/apache2/sites-enabled/000-default.conf
ADD ./assets/apache/servername.conf  /etc/apache2/conf-enabled/servername.conf
RUN a2enmod rewrite proxy proxy_http proxy_connect ssl proxy_html deflate headers

# Finishing touches
ADD ./assets/flag.txt /var/www/html/flag.txt
RUN apt-get clean
EXPOSE 80

# for some reason services won't start, even Apache with `service apache2 start`. We run them here as we need an entrypoint anyway.
ADD ./entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
