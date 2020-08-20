# UdacityCapstone
 
# Restaurant Manager API for Arena Delivery Business

## Overview
This is the capstone project of the Udacity Full Stack Nanodegree. It covers the following topics. 

### Installing Dependencies Locally

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

I recommend working within a virtual environment. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Setup the Database
Change the database path in models.py to your local instance of postgres database. 

`database_path = os.environ['DATABASE_URL']`

Make sure to include username, password, and port. 

## Authentication

Please use the following two bearer tokens for Auth0 authentication to test the endpoints via Postman. 

`Bearer Token 1 = eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Imh6ZFpjb3A2LWRBcGxTUmdiaWJpWiJ9.eyJpc3MiOiJodHRwczovL2Rldi0xM3B1NGhkMS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYwYjU5MGEzZTBkZTgwMDEzYTlhYzNjIiwiYXVkIjoicmVzdGF1cmFudCIsImlhdCI6MTU5Nzg2OTYwNSwiZXhwIjoxNTk3ODc2ODA1LCJhenAiOiJEZHBPTjQ0SFBHQlMwOWI3V2xCbm9PejV6VmN5aGk0SCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiYWRkOmFyZW5hcyIsImFkZDptZW51cyIsImFkZDpyZXN0YXVyYW50cyIsImVkaXQ6cmVzdGF1cmFudHMiLCJyZWFkOmFyZW5hcyIsInJlYWQ6IG1lbnVzIiwicmVhZDpyZXN0YXVyYW50cyJdfQ.X3hSkj1DJ6vJPF_tKqLmxAbSZN1NW8W3HFP-9U62ami5DrFRnXj6yqHVTPOk0S21_nFp6oRkxcULneQtSXLgBWifFJBJ0LztVfR8v5SjYfwrU_5dS_Vvk-nzdTajvzoOoHQ8cuzEqmNbE0dOfqEEeib4SKP92-ZpZ_QzzJQdiq1LWwrvRi7oAYElD7FgLQSKQSUQN9gvWxVi0UnANLCNLjB423tZ2ddsZV7LJEuDNxHhgE0Nukf7yXXHRsyZgr3CxTUQ-xN-ufKpJeQoFaUjXKaE6c5AKshJt145GyDmK4gAUOa7OXfGFCrbrEy0n7GcolCLMNi-MA5Lt-M_ZG5Lvw`

`Bearer Token 2 =`


## Running the server

From within the directory first ensure you are working using your created virtual environment.

To run the server, execute:

```
SET FLASK_APP=app
SET FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Running the Postman Tests


To run the flask tests, run the following command:
python -m unittest discover -t ../

## API Documentation

* GET "/arenas"
    - Fetches a list of Arenas that exist in the database
    - Request Parameters: Bearer Token 1 or 2
    - Response Body:
    
    {
  "arenas": [
    {
      "name": "Amalie Arena,
      "address": "Test",
      "id": 1
    },
    {
      "name": "Raymond James,
      "address": "Test",
      "id": 2
    }
  ],
  
  "success": true
}

```

* GET "/arenas/<int:id>"
    - Fetches a single arena by the ID
    - Request Parameters: `id` 
    - Response Body:
```json
{
  "arenas": [
    {
      "name": "Amalie Arena,
      "address": "Test",
      "id": 1
    }
  ],
  
  "success": true
}
```

* POST "/restaurants"
    - Posts a new restaurant to the datbase
    - Request Headers: (application/json) 1. string name (required) 2. string address (required) 3. integer arena_id
    - Returns:
```json
{
    "name": "McDonalds",
    "success": true
}
```

* GET "/arenas/<int:id>/restaurants"
    - Fetches all restaurants by arena id
    - Request Parameters: `arena_id`: arena id for which you want to see a list of restaurants.
    - Response Body:
```json
{
  "restaurants": [{
      "restaurant_id": 1,
      "name": "McDonalds",
      "address": "124 amalie way",
      "arena_id": 1,
      "menu": "Dinner",
      "customer":"null",
      "order": "null"
  }]
```

* POST "/menus/create"
    - Creates a new menu within a
    - Request Body:
```json
{
  "name":"Lunch",
  "restaurant_id":1
}
```

* PATCH "/menus/<int:id>/edit"
    - Change the name of an existing menu
    - Request Body:
```json
{
  "name":"Dinner",
  "restaurant_id":1
}
```
* GET "/restaurants/<int:id>/menus"
    - Fetches all menus within a restaurant
    - Request Parameters: `id`: restaurant_id for which you want to see a list of menus.
    - Response Body:
```json
{
  "menus": [{
      "menu_id": 1,
      "menu_name": "Dinner",
      "restaurant_id": 1,
      "menu_item": [{
          "id":1,
          "name":"Chicken Tenders",
          "menu_id":1
      }]
  }]
```
* DELETE "/menus/<int:menu_id>"
    - Removes the selected menu from the restaurant
    - Request Parameters: `id`: menu_id for which you want to delete
    - Response Body:
```json
{
  "deleted_menu": 1,
  "success" "True"
  }
```

