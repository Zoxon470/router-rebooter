FROM python:3.8-alpine

WORKDIR /rebooter

COPY crontab /etc/cron.d/rebooter-cron
RUN chmod 0644 /etc/cron.d/rebooter-cron
RUN touch /var/log/cron.log

RUN apk update
RUN apk add chromium chromium-chromedriver dcron

COPY . .

RUN pip install selenium==3.141.0

CMD crond -s /etc/cron.d -b -L /var/log/cron.log && tail -f /var/log/cron.log
