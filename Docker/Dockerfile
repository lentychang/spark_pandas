FROM openjdk:8-alpine
#FROM adoptopenjdk/openjdk8:debian-slim

ARG DAEMON_RUN=true
ARG SPARK_VERSION=2.4.4
ARG HADOOP_VERSION=2.7
ENV SCALA_VERSION=2.12.4
ENV SCALA_HOME=/usr/share/scala

RUN apk add --no-cache --virtual=.build-dependencies wget ca-certificates && \
    apk add --no-cache bash curl jq
RUN  cd "/tmp" && \
    wget --no-verbose "https://downloads.typesafe.com/scala/${SCALA_VERSION}/scala-${SCALA_VERSION}.tgz" && \
    tar xzf "scala-${SCALA_VERSION}.tgz" && \
    mkdir "${SCALA_HOME}" && \
    rm "/tmp/scala-${SCALA_VERSION}/bin/"*.bat && \
    mv "/tmp/scala-${SCALA_VERSION}/bin" "/tmp/scala-${SCALA_VERSION}/lib" "${SCALA_HOME}" && \
    ln -s "${SCALA_HOME}/bin/"* "/usr/bin/" && \
    apk del .build-dependencies && \
    rm -rf "/tmp/"*
    
#Scala instalation
RUN export PATH="/usr/local/sbt/bin:$PATH" &&  apk update && apk add ca-certificates wget tar && mkdir -p "/usr/local/sbt" && wget -qO - --no-check-certificate "https://cocl.us/sbt-0.13.16.tgz" | tar xz -C /usr/local/sbt --strip-components=1 && sbt sbtVersion

RUN apk add --no-cache python3

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
