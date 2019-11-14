FROM python:3.7
RUN mkdir /opt/django_test
WORKDIR /opt/django_test
COPY requirements.txt /opt/django_test
RUN pip install -r requirements.txt
COPY . /opt/django_test
ENTRYPOINT ["/opt/django_test/docker-entrypoint.sh"]
