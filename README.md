# UdacityCapstone
 
# Restaurant Manager API for Arena Delivery Business

## Overview
This is the capstone project of the Udacity Full Stack Nanodegree. It covers the following topics. 

### Motivation
I have been putting together a business idea to create a delivery service within arenas. This is the perfect opportunity to start building out the backend of the MVP. The business concept has two key elements the first of which is a system to allow restaurants to manage inventory. 

The restaurant manager API is the intial build out of the concept. 

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

### Setup the Database
Change the database path in models.py to your local instance of postgres database. 

`database_path = os.environ['DATABASE_URL']`

Make sure to include username, password, and port. 

### Running the server

From within the directory first ensure you are working using your created virtual environment.

To run the server, execute:

```
SET FLASK_APP=app
SET FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

### Running the Postman Tests


To run the flask tests, run the following command:
python -m unittest discover -t ../

## API Documentation

#### GET /arenas

`$ curl -X GET https://restaurant-manager-api.herokuapp.com/arenas`

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

#### POST /arenas

`$ curl -X POST https://restaurant-manager-api.herokuapp.com/arenas`

* POST "/arenas"
    - Adds a new arena
    - Request body: Bearer token 1
    
    {
      "name": "Amalie Arena,
      "address": "Test"
    },

#### GET /arenas/<int:id>

`$ curl -X GET https://restaurant-manager-api.herokuapp.com/arenas/1`

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

#### POST /restaurants

`$ curl -X POST https://restaurant-manager-api.herokuapp.com/arenas`

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
#### GET /arenas/<int:id>/restaurants

`$ curl -X GET https://restaurant-manager-api.herokuapp.com/arenas/1/restaurants`

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
#### POST /menus/create

`$ curl -X POST https://restaurant-manager-api.herokuapp.com/menus/create`

* POST "/menus/create"
    - Creates a new menu within a
    - Request Body:
```json
{
  "name":"Lunch",
  "restaurant_id":1
}
```

#### PATCH /menus/<int:id>/edit

`$ curl -X PATCH https://restaurant-manager-api.herokuapp.com/menus/1/edit`

* PATCH "/menus/<int:id>/edit"
    - Change the name of an existing menu
    - Request Body:
```json
{
  "name":"Dinner",
  "restaurant_id":1
}
```
#### GET /restaurants/<int:id>/menus

`$ curl -X GET https://restaurant-manager-api.herokuapp.com/restaurants/1/menus`

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
#### DELETE /menus

`$ curl -X DELETE https://restaurant-manager-api.herokuapp.com/menus/1`

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

## Authentication

All API Endpoints are decorated with Auth0 permissions. To use the project locally, you need to config Auth0 accordingly

### Auth0 for locally use
#### Create an App & API

1. Login to https://manage.auth0.com/ 
2. Click on Applications Tab
3. Create Application
4. Give it a name like `Music` and select "Regular Web Application"
5. Go to Settings and find `domain`. Copy & paste it into config.py => auth0_config['AUTH0_DOMAIN'] (i.e. replace `"example-matthew.eu.auth0.com"`)
6. Click on API Tab 
7. Create a new API:
   1. Name: `Music`
   2. Identifier `Music`
   3. Keep Algorithm as it is
8. Go to Settings and find `Identifier`. Copy & paste it into config.py => auth0_config['API_AUDIENCE'] (i.e. replace `"Example"`)

#### Create Roles & Permissions

1. Before creating `Roles & Permissions`, you need to `Enable RBAC` in your API (API => Click on your API Name => Settings = Enable RBAC => Save)
2. Also, check the button `Add Permissions in the Access Token`.
2. First, create a new Role under `Users and Roles` => `Roles` => `Create Roles`
3. Give it a descriptive name like `Casting Assistant`.
4. Go back to the API Tab and find your newly created API. Click on Permissions.
5. Create & assign all needed permissions accordingly 
6. After you created all permissions this app needs, go back to `Users and Roles` => `Roles` and select the role you recently created.
6. Under `Permissions`, assign all permissions you want this role to have. 

# <a name="authentification-bearer"></a>
### Auth0 to use existing API
If you want to access the real, temporary API, bearer tokens for all 3 roles are included below:

#### Admin

"Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Imh6ZFpjb3A2LWRBcGxTUmdiaWJpWiJ9.eyJpc3MiOiJodHRwczovL2Rldi0xM3B1NGhkMS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYwYjU5MGEzZTBkZTgwMDEzYTlhYzNjIiwiYXVkIjoicmVzdGF1cmFudCIsImlhdCI6MTU5NzkzNjUzNywiZXhwIjoxNTk3OTQzNzM3LCJhenAiOiJEZHBPTjQ0SFBHQlMwOWI3V2xCbm9PejV6VmN5aGk0SCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiYWRkOmFyZW5hcyIsImFkZDptZW51cyIsImFkZDpyZXN0YXVyYW50cyIsImRlbGV0ZTptZW51cyIsImVkaXQ6bWVudXMiLCJlZGl0OnJlc3RhdXJhbnRzIiwicmVhZDphcmVuYXMiLCJyZWFkOiBtZW51cyIsInJlYWQ6cmVzdGF1cmFudHMiXX0.tN01CYRPUhQJ3AA322pgy-NiFI7JLpTQBQHd5KSmi-oL6EMjdslxficH6Z-9pCFSsd-_EbryDs9tlszn8zXBhgxAMi6p1_LfiHZVS3ATw-DesxuBPQvftMsmK3oyoq5QZJmflbxtizz_7G9zpOy0kdccPKSFCzVfly3KRKNWs6jKeII6_92yPtidan6l8lXW-menYF1o77TakiR2THzvxKHDwD-2UL5na2qUCSCyquPGWzw7obeMSqomMItGGU-dH70KKiV2ZaC7U6q6roP1F1MgPZy1iH9LZPZsVmlgPy_SG8zbIHe-I7C-Z6ts5fZwP6MtAIwvmbC0RPsM8PV9ww"

#### Restaurant Admin

"Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Imh6ZFpjb3A2LWRBcGxTUmdiaWJpWiJ9.eyJpc3MiOiJodHRwczovL2Rldi0xM3B1NGhkMS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVmYThkZTI4OTgxNzQwMDEzZGFhNGNkIiwiYXVkIjoicmVzdGF1cmFudCIsImlhdCI6MTU5NzkzNjcxOSwiZXhwIjoxNTk3OTQzOTE5LCJhenAiOiJEZHBPTjQ0SFBHQlMwOWI3V2xCbm9PejV6VmN5aGk0SCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiYWRkOm1lbnVzIiwiYWRkOnJlc3RhdXJhbnRzIiwiZGVsZXRlOm1lbnVzIiwiZWRpdDptZW51cyIsImVkaXQ6cmVzdGF1cmFudHMiLCJyZWFkOmFyZW5hcyIsInJlYWQ6IG1lbnVzIiwicmVhZDpyZXN0YXVyYW50cyJdfQ.DaIBmYXlU81DOqUpXvaXBhQapTQYX6b8bhaa86aIg57PVTB0Xy4Jtc3rP5YLWhVN9aL8i8a4USKf63TYB4-L4VcEUOMf3uCtziec3aBeNJKArd1q_YE9c9Z3OON3BcOr6jsZd2rb9-RfClqxbexysBf8UOkQGRq6Ps-vnceRT8QPu0q3xD-bN1dQ87MYwpZNi9B-7rod5gdb_qcwH6D0uT4U3P80YZocvdirsW-mGnz3fXP8khUNnh7WTkPh05xMNKol_EvsICM-6K9XcNj_Pnfm391dWs9vRxaMB1tCNtHMcj6dXJjPFQj-YFgISfZcnJiu0wxFb04hFXHcbSOVbg"

## Existing Roles

They are 2 Roles with distinct permission sets:

1. Admin (all actions):
  - GET /arenas (read:arenas) Can read all arenas
  - GET /menus (read:menus) Can read all menus 
  - GET /restaurants (read:restaurants) Can read all restaurants
  - POST /arenas (add:arenas) Can create new arenas
  - POST /menus/create (add:menus) Can create new menus
  - POST /restaurants (add:restaurants) Can create new restaurants
  - PATCH /resetaurants (edit:restaurants) Can edit existing restaurants
  - PATCH /menus (edit:menus) Can edit existing menus
  - DELETE /menus (delete:menus) Can remove a menu
2. Restaurant Admin (can do everything except adding a new arena)
  - GET /arenas (read:arenas) Can read all arenas
  - GET /menus (read:menus) Can read all menus 
  - GET /restaurants (read:restaurants) Can read all restaurants
  - POST /menus/create (add:menus) Can create new menus
  - POST /restaurants (add:restaurants) Can create new restaurants
  - PATCH /resetaurants (edit:restaurants) Can edit existing restaurants
  - PATCH /menus (edit:menus) Can edit existing menus
  - DELETE /menus (delete:menus) Can remove a menu

In your API Calls, add them as Header, with `Authorization` as key and the `Bearer token` as value. Don´t forget to also
prepend `Bearer` to the token (seperated by space).

For example: (Bearer token for `Admin`)
```js
{
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik16azVRVUk0TXpSR04wSXhOVU13TkRrME16QXdNMFpHTmtFMU1VWXdPRUpCTmpnMFJrVTBSZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtbWF0dGhldy5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU0N2VmYzc2N2YxYmEwZWJiNDIwMTYzIiwiYXVkIjoiTXVzaWMiLCJpYXQiOjE1ODE4NjI0NjksImV4cCI6MTU4MTg2OTY2OSwiYXpwIjoiVGh2aG9mdmtkRTQwYlEzTkMzSzdKdFdSSzdSMzFOZDciLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTphY3RvcnMiLCJjcmVhdGU6bW92aWVzIiwiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJlZGl0OmFjdG9ycyIsImVkaXQ6bW92aWVzIiwicmVhZDphY3RvcnMiLCJyZWFkOm1vdmllcyJdfQ.iScamWOFNx9pjiVZhsvPzDoRi6EraZaxWg-WMj80HNW_-dchkOymnKA7OOhPQ8svLc9-wViLlCT-ySnupZ-209cIBVHSA_slncSP-lzEM6NKbBmDEETTQ1oxv2jTH-JL72eLhyAWUsmSIZDmEab1hln1yWEN7mUnn0nZJfxCRCs89h5EGJzXS2v8PbAjq9Mu7wFsrioEMx_PGWzSM0r5WIrKBvpXRy0Jm-vssZl4M1akDHIL5Shcfp_Bfnarc2OLOMvdQVHVDEWhrbFSnfCENLDxkcmB18VnOedJAuY_C88YRUfY2wQAOPux8RVuqIb5KxTg4YP7kiDcBUKXEnhL9A"
}
```