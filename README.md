# Info display

To run project you need docker and docker-compose installed on your machine.

To run, execute

```
docker-compose up
```

Info display is server from http://localhost:8080/

Backend containers are proxied through http://localhost:9090/[container label in compose-file]/. for example http://localhost:9090/first/

Backend needs to return JSON, with title and content fields. 

```
{"title": "Page title, printed on TITLE tag", "content":"Page content, printed inside BODY"}
```

Because of PHP, control characters may break the JSON parsing. That's why \n are removed, and \t replaced with four spaces. 
