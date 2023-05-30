### Warehouse:
In this app there are 3 models (Supplier, Product and Category) to save and control products. The idea is to let users reserve certain amount of a product and after finishing their payment subtract the reserved amount from the whole. This way we can make sure that we can prevent distributed data problem.

### Missing part
There is one more thing to implement in order to complete this project. After we reserve a product we need a way to expire reservation after a certain amount of time. I could use Celery in order to check every order periodically to see if it has expired or not.

### Tools used in this service

- Framework: Flask
- Dataase: MySql
- ORM: SqlAlchemy
- Message queue: rabbitmq
- testing: pytest

### How to run (rollup)
Everthing has dockerized So you need to just run command below:

```
docker compose up -d
```

NOTE: In old versions the command was like this ```docker-compose ... ``` so if you encountered an error give it a try.
