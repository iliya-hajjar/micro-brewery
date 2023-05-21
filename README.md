This is a microbrewery project under the name projectok. This whole project consists of 3 services Accounting, Sales and Warehouse. I've started 
to code this project on 18th of May and spent 4-5 days up to this point.

### Techincal details of the project

All three services dockerzied and as database I use MySql for all the services. Technical details of each services are as follows:

### Sales:
- Framework: Flask
- Dataase: MySql
- ORM: SqlAlchemy
- Pub/Sub: rabbitmq

### Warehouse:
- Framework: Flask
- Dataase: MySql
- ORM: SqlAlchemy
- Pub/Sub: rabbitmq

### Sales:
- Framework: Django
- Dataase: MySql
- ORM: Django
- Pub/Sub: rabbitmq
- API: DRF (exposing by Swagger)

And the whole schema of the project :

![Alt text](cloudsigma.png?raw=true "Schema")