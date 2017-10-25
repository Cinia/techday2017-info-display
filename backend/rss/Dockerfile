FROM maven:3.5.0-jdk-8-alpine as BUILD
COPY . /app
WORKDIR /app
RUN mvn package

FROM openjdk:8-jre-alpine
WORKDIR /app
COPY --from=BUILD /app/target/rss-0.0.1.jar .
ENTRYPOINT exec java -Djava.security.egd=file:/dev/./urandom -jar rss-0.0.1.jar