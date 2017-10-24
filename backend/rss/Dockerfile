FROM openjdk:8-jdk-alpine
VOLUME /tmp
ADD target/rss-0.0.1.jar rss.jar
ENV JAVA_OPTS=""
ENTRYPOINT exec java $JAVA_OPTS -Djava.security.egd=file:/dev/./urandom -jar /rss.jar
