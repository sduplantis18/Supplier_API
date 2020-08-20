import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import db, setup_db, Arena, Restaurant, Customer, Shipment, Menu, Menu_Item, Order, Runner, db_drop_and_create_all
from config import bearer_tokens
from sqlalchemy import desc
from datetime import date

# Create Authorization key and Bearer token as values from config file
admin_auth_header = {
    'Authorization': bearer_tokens['Admin']
}

restaurant_manager_auth_header = {
    'Authorization': bearer_tokens['Restaurant Manager']
}


class RestaurantAPITests(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.environ['DATABASE_URL']
        setup_db(self.app, self.database_path)
        db_drop_and_create_all()

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()
        
    def tearDown(self):
        pass

    '''
    tests
    '''
    #test successful create arena
    def test_create_arena(self):
        arena = {
            'name' : "Amalie",
            'address': "123 amalie way"
        }

        res = self.client().post('/arenas', json = arena, headers = admin_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
    
    #test fail create arena with no auth header
    def test_create_arena_fail(self):
        arena = {
            'name' : "Tropicana Field",
            'address': "123 amalie way"
        }

        res = self.client().post('/arenas', json = arena)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    #test fail for get arena (ensure there are no arenas when running this test)
    def test_get_arena_fail(self):
        res = self.client().get('/arenas', headers = admin_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success']) 
    

    #test pass for get arena 
    def test_get_arena_pass(self):
        res = self.client().get('/arenas',  headers = admin_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertFalse(data['success']) 

    #test fail for get restaurant
    def test_fail_get_restaurants(self):
        res = self.client().get('/arenas/300/restaurants',  headers = admin_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    #test fail for post new restaurant with no auth
    def test_fail_post_restaurant(self):

        restaurant = {
            'name' : "Tropicana Field",
            'address': "123 amalie way"
        }

        res = self.client().post('/restaurants', json = restaurant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    #test pass for post new restaurant
    def test_pass_post_restaurant(self):
        restaurant = {
            'name' : "Tropicana Field",
            'address': "123 amalie way"
        }

        res = self.client().post('/restaurants', json = restaurant,  headers = admin_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

        
    
if __name__ == "__main__":
    unittest.main()