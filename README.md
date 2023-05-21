This is a microbrewery project under the name projectok. This whole project consists of 3 services Accounting, Sales and Warehouse. I've started 
to code this project on 18th of May and spent 4-5 days up to this point.

## Techincal details of the project

All three services dockerzied and as database I use MySql for all the services. Technical details of each services are as follows:

### Sales:
- Framework: Flask
- Dataase: MySql
- ORM: SqlAlchemy
- Pub/Sub: rabbitmq
- testing: pytest

### Warehouse:
- Framework: Flask
- Dataase: MySql
- ORM: SqlAlchemy
- Pub/Sub: rabbitmq
- testing: pytest

### Sales:
- Framework: Django
- Dataase: MySql
- ORM: Django
- Pub/Sub: rabbitmq
- API: DRF (exposing by Swagger)
- testing: native of django


And the whole schema of the project :

![Alt text](cloudsigma.png?raw=true "Schema")

### Version of the tools used for this project

Ubuntu: 22.04LTS
docker: 23.0.6
docker compose: 2.17.3
python: 3.9


### My goal

My goal was to add one more service auth as an API gateway but with the time I've got this was all I could do.

### Improvementa

1- Complete test for all services
2- 
