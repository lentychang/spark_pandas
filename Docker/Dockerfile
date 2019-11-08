FROM openjdk:8-alpine
FROM adoptopenjdk/openjdk8:debian-slim

ARG DAEMON_RUN=true
ARG SPARK_VERSION=2.4.4
ARG HADOOP_VERSION=2.7

RUN apk --update add wget tar bash
RUN wget http://apache.mirror.anlx.net/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz
RUN tar -xzf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz && \
    mv spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} /spark && \
    rm spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz
COPY start-master.sh /start-master.sh
COPY start-worker.sh /start-worker.sh

RUN apk add --no-cache --virtual .build-deps g++ python3-dev libffi-dev openssl-dev &&\
    apk add --no-cache --update python3 &&\
    pip3 install --upgrade pip setuptools
RUN pip3 install pandas
