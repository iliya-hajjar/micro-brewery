This is a microbrewery project under the name projectok. This whole project consists of 5 services Accounting, Sales, Warehouse, Auth and API_gateway. All services need authentication and there is no access to the services from outside. The whole communication is through gateway which is using flask and NGINX. I've started to code this project on 18th of May and spent 7-8 days up to this point.

## Techincal details of the project

All three services dockerzied and as a database I useed MySql for all the services. Technical details of each services are as follows:

### Sales:
- Framework: Flask
- Dataase: MySql
- ORM: SqlAlchemy
- Message queue: rabbitmq
- testing: pytest

### Warehouse:
- Framework: Flask
- Dataase: MySql
- ORM: SqlAlchemy
- Message queue: rabbitmq
- testing: pytest

### Sales:
- Framework: Django
- Dataase: MySql
- ORM: Django
- Message queue: rabbitmq
- API: DRF (exposing by Swagger)
- testing: native of django

### Auth:
- Framework: Flask
- Dataase: MySql
- ORM: SqlAlchemy

### API_gateway:
- Framework: Flask
- Web server: NGINX


And the whole schema of the project :

![Alt text](cloudsigma.png?raw=true "Schema")

### Version of the tools used for this project

- Ubuntu: 22.04LTS
- docker: 23.0.6
- docker compose: 2.17.3
- python: 3.9


### Improvements

- Complete tests for all services
- Add CI/CD pipeline
- Add precommit to apply flake8 and black
- Add manager to all SqlAlchemy based services to have migrations
- Add logger
