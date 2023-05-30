### Accounting:
In this app there are 2 models (Transaction and Payment) to save and control accounting. This app is responsible for payments. On every order from sales it will set an transaction and will confirm payment after confirmation it will send a request sales and sales will update ware house (telling warehouse that the it can reduce the available amount from the whole and reduce amount from reserved field).

### Missing part
Here I use an endpoint to update (PUT) on Transaction to set is_confirmed to True which is not the case in real world. The solution is to set a Celery task to handel confirmation on a transaction and if everything was ok send a message back to sales.

### Tools used in this service

- Framework: Django
- Dataase: MySql
- ORM: Django
- Message queue: rabbitmq
- API: DRF (exposing by Swagger)
- testing: native of django

### How to run (rollup)
Everthing has dockerized So you need to just run command below:

```
docker compose up -d
```

NOTE: In old versions the command was like this ```docker-compose ... ``` so if you encountered an error give it a try.
