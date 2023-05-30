### Authentication
In this app is only model (User) to save and control orders. This model keeps email(as a username) and password. 

### Improvement
First we could use rules for each type of user to let each type has its own access url, for example using ACL and define url for each user.

### Tools used in this service

- Framework: Flask
- Dataase: MySql
- ORM: SqlAlchemy

### How to run (rollup)
Everthing has dockerized So you need to just run command below:

```
docker compose up -d
```

NOTE: In old versions the command was like this ```docker-compose ... ``` so if you encountered an error give it a try.
