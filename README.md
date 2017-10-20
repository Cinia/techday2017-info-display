# Info display

To run project you need docker and docker-compose installed on your machine.

To run, execute

```
docker-compose up
```

Info display is server from http://localhost:8080/

Backend containers are proxied through http://localhost:9090/[container label in compose-file]/. for example http://localhost:9090/first/
