FROM python:3.9-alpine
RUN sed -i 's/https/http/' /etc/apk/repositories
RUN apk add curl
WORKDIR /data/meetingroom
ENV server_params=
COPY requirements.txt ./
RUN apk add --update --no-cache curl jq py3-configobj py3-pip py3-setuptools python3 python3-dev \
  && apk add --no-cache gcc g++ jpeg-dev zlib-dev libc-dev libressl-dev musl-dev libffi-dev \
  && python -m pip install --upgrade pip \
  && pip install -r requirements.txt \
  && apk del gcc g++ libressl-dev musl-dev libffi-dev python3-dev \
  && apk del curl jq py3-configobj py3-pip py3-setuptools \
  && rm -rf /var/cache/apk/*
COPY . .
EXPOSE 8000
CMD ["/bin/sh", "/data/meetingroom/start.local.bat"]