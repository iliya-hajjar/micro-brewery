### Introduction

This is a microbrewery project under the name projectok. This whole project consists of 5 services Accounting, Sales, Warehouse, Auth and API_gateway. All services need authentication and there is no access to the services from outside. The whole communication is through gateway which is using flask and NGINX. Although the tests are must, I could not complete tests for all projects because I could spend only enough time to implement my idea. I've started to code this project on 18th of May and spent 7-8 days up to this point overall.

## Techincal details of the project

All three services dockerzied and as a database I used MySql for all the services. Diagram of the whole project:


![Alt text](microservices.png?raw=true "Schema")

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


### Recommended improvements

- As administrator of the system I want to add a new item in Warehouse
- As Administrator of the system I want to put a price of an item in the warehouse
- As user of the system I want to buy maximum quantity of given item
- As user of the system I want to see an error message if the quantity available is insufficient
