FROM openjdk:8
VOLUME /tmp
ADD . /app
WORKDIR /app
RUN apt-get update && apt-get -y upgrade && apt-get install -y maven && mvn package
ENV JAVA_OPTS=""
ENTRYPOINT exec java $JAVA_OPTS -Djava.security.egd=file:/dev/./urandom -jar /app/target/rss-0.0.1.jar
