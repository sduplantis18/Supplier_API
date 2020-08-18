# UdacityCapstone
 
# Restaurant Manager API for Arena Delivery Business

## Overview

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

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

##Running the Postman Tests


To run the flask tests, run the following command:
python -m unittest discover -t ../

## API Documentation

* GET "/categories"
    - Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
    - Request Parameters: None
    - Response Body:
    
    `categories`:{
    '1' : "Science",
    '2' : "Art",
    '3' : "Geography",
    '4' : "History",
    '5' : "Entertainment",
    '6' : "Sports"}

```

* GET "/questions?page=1"
    - Fetches the questions to be displayed on the page using page number
    - Request Parameters: `page`: Page number
    - Response Body:
```json
{
  "questions": [{
    "id": 1,
    "question": "",
    "answer": "",
    "category": 1,
    "difficulty": 1
  }],
  "categories": {
    "1": "Science",
    "2": "Art"
  },
  "total_questions": 1
}
```

* DELETE "/questions/<int:question_id>"
    - Deletes a question from the database
    - Request Parameters: `question_id`: Question ID to delete
    - Response Body:
```json
{
  "deleted": 20
}
```

* POST "/questions"
    - Adds a questions to the database
    - Request Body:
```json
{
  "question": {
    "id": 1,
    "question": "",
    "answer": "",
    "category": 1,
    "difficulty": 1
  }
}
```

* POST "/search"
    - Fetches questions based on the search term
    - Request Body:
```json
{
  "questions": [{
    "id": 1,
    "question": "",
    "answer": "",
    "category": 1,
    "difficulty": 1
  }],
  "total_questions": 1
}
```

* GET "/categories/<int:category_id>/questions"
    - Fetches questions for the requested category
    - Request Parameters: `category_id`: Category ID for questions
    - Response Body:
```json
{
  "questions": [{
    "id": 1,
    "question": "",
    "answer": "",
    "category": 1,
    "difficulty": 1
  }],
  "total_questions": 1,
  "current_category": 1
}
```

* POST "/quizzes"
    - Fetches a unique question for the quiz on selected category
    - Request Body:
```json
{
  "question": {
    "id": 1,
    "question": "",
    "answer": "",
    "category": 1,
    "difficulty": 1
  }
}
```