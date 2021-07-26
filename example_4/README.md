# Exercise 4

## Requirements:

Make sure that you are in the current directory.

Install [docker](https://docs.docker.com/engine/install/)

Install [docker-compose](https://docs.docker.com/compose/install/)

You can install the requirements or simply develop on docker.
```sh
pip install -r requirements.txt

```
### Start the containers

To run all services:
```sh
make up
```
### Test

To run all tests:
```sh
make test-all
```

### End2end test:

Start the containers:

```sh
make up
```

Run the test:

```sh
make test-end2end
```
### Stop the containers:

```sh
make stop
```
## Exercise 4

In this exercise we are going to build an api to show some concepts of the test pyramid, the api will have similar functions to the applications we build in exercise 1 and 3. It has three endpoints:

- (/operations/sum/x/x) to return the addition of two numbers.
- (/operations/sub/x/x) to return the subtraction of two numbers.
- (/operations/fac/x) to return the factorial of two numbers.

In addition, all the operations made by the applications are stored in a database, al the api can return the operation and the result using the endpoint ```/<id:int>```, the id is the identifier of the application.
To develop this example, we are going to use flask as the backend with sqlalchemy and postgres. This repository is preloaded with the frontend of the application in the [/client](./client) directory so to run the test you can use this frontend, to start the frontend you should cd into client (```cd client```), ```npm start``` to install the dependencies and ```ng serve``` to start the frontend. In addition, you can use the dockerized containers to develop this exercise, to do this you can do  ```make up``` to start the client, the api and the postgres db.

The tests that we are going to perform to complete the exercise are this:

![Test](./../docs/static/images/test_4.jpg)

The process that we are going to follow is, write the highest-level test and mock every thing under it, once everything pass, we can go to the next level, write the test, write the code to pass the test and re-write the tests of the highest levels to use the code we have implemented. So if you follow this approach, you should start with the end2end test.

### end2end tests

To do this, you can use selenium, this test is going to make request to every endpoint and mock the response.

## Solution

Remember that you can always check a possible solution in:

```sh
git checkout Exercise_4_Solution
```