### Authentication
This app has no model instead it is a gateway to the outside world and inside. Also responsible for security, thats why I used NGINX here to expose only port 80.

### Tools used in this service

- Framework: Flask
- Web server: NGINX

### How to run (rollup)
Everthing has dockerized So you need to just run command below:

```
docker compose up -d
```

NOTE: In old versions the command was like this ```docker-compose ... ``` so if you encountered an error give it a try.
