# Scraping ads-website

# Built With

> ### `Python`
> ### `PostgreSQL` 
> ### `Poetry`

---
# Getting started
---
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
# Prerequisites
1. Clone the repository
```
https://github.com/luianqi/kijiji-scraping.git
```
2. Install poetry.lock
```
Poetry install 
```
3. Create a new PostgreSQL database

4. In your terminal:
```
psql postgres
CREATE DATABASE databasename
\c databasename
```
5. Build the Docker Image
```
$ docker-compose build 
```
9. Run the project
```
$ docker-compose up
```
And the scraped data will show up in your database
