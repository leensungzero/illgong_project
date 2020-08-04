FROM python:3.7

RUN apt-get update -qq \
    && apt-get install -y --no-install-recommends libmariadb-dev-compat libmariadb-dev \
    ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime

RUN mkdir -p /opt/services/illgong/src
WORKDIR /opt/services/illgong/src

COPY requirements/development.txt /opt/services/illgong/src
RUN pip install -r requirements/development.txt

COPY . /opt/services/ttsapi/src

RUN python3 manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "scheduler.wsgi:application", "--timeout", "1000"]