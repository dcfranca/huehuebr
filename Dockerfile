FROM dockerfiles/django-uwsgi-nginx

RUN apt-get update \
        && apt-get install -y libmysqlclient-dev \
        && rm -fr /var/lib/apt/lists/* \
        && rm -fr /tmp/* \
        && rm -fr /var/tmp/*


ADD ./backend/app /home/docker/code/app
ADD ./backend/uwsgi.ini /home/docker/code/uwsgi.ini
WORKDIR /home/docker/code/app
RUN pip3 install -r requirements.txt

EXPOSE 80 8000