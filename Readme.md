# ALU Tech Assesment

## Introduction

[![Build Status](https://travis-ci.org/lennykamande/alu-test.svg?branch=main)](https://travis-ci.org/lennykamande/alu-test) [![Coverage Status](https://coveralls.io/repos/github/lennykamande/alu-test/badge.svg?branch=main)](https://coveralls.io/github/lennykamande/alu-test?branch=main)

## Run in Postman

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/ce5fa5121eb851f81114)

### Features

1. Users can create an account
2. Users can login
3. Users can logout

### Installing

_Step 1_

Create directory
`$ mkdir alu-test`

`$ cd alu-test`

Create and activate virtual environment

`$ virtualenv env`

`$ source env/bin/activate`

Clone the repository [`here`](https://https://bitbucket.org:lennymanyeki/alu-test.git) or

` git clone git@bitbucket.org:lennymanyeki/alu-test.git`

Install project dependencies

`$ pip install -r requirements.txt`

_Step 2_

#### Set up database and virtual environment & Database

Go to postgres terminal and create the following databases

Main database

`# CREATE DATABASE database_name ;`

Test database

`# CREATE DATABASE test_database_name ;`

_Step 3_

#### Storing environment variables

```
export FLASK_APP="run.py"
export APP_SETTINGS="development"
export DATABASE_URL="dbname='lenny' host='localhost' port='5432' user='postgres' password='root'"
export DATABASE_TEST_URL="dbname='test_database_name' host='localhost' port='5432' user='postgress' password='root'"
```

_Step 4_

#### Running the application

`$ python run.py`

_Step 5_

#### Testing

`$ nosetests app/tests`

### API-Endpoints

#### Users Endpoints : /api/v1/

| Method | Endpoint     | Functionality         |
| ------ | ------------ | --------------------- |
| POST   | /auth/signup | Create a user account |
| POST   | /auth/login  | Sign in a user        |
| POST   | /auth/logout | Sign out a user       |
