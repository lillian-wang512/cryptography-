FROM python:3.7
MAINTAINER c4pr1c3

COPY ./src/requirements.txt /tmp

RUN pip install -i "https://pypi.tuna.tsinghua.edu.cn/simple" -r /tmp/requirements.txt && useradd -m flask

WORKDIR /flask

USER root

EXPOSE 443

