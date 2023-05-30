### Sales
In this app there are 3 models (Order and OrderDetails) to save and control orders. We fill Order and OrderDetails in one place for one order (request data for both and the backend will handel the rest). 

### Improvement
There is an improvement here we could have a way to send batch of order instead of single order this way we could reduce requests.

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
