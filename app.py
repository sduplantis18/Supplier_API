import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, setup_db, Arena, Restaurant, Customer, Shipment, Menu, Menu_Item, Order, Runner, db_drop_and_create_all

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  @app.after_request
  def after_request(response):
      response.headers.add('Access-Control-Allow-Headers','Content-Type,Authorization,true')
      response.headers.add('Access-Control-Allow-Methods','GET,PUT,POST,DELETE,OPTIONS')
      response.headers.add('Access-Control-Allow-Origin', '*')
      return response

  #API routes
  '''
  Get list of all arenas
  '''
  @app.route('/arenas', methods=['GET'])
  def get_arenas():
    arenas = Arena.query.order_by(Arena.id).all()
    total_arenas = len(arenas)
    if total_arenas == 0:
      abort(404)

    arena_list = [arena.format() for arena in arenas]
    
    return jsonify ({
      'success':True,
      'arenas': arena_list 
    }), 200

  '''
  create a new arena
  '''
  @app.route('/arenas', methods=['POST'])
  def add_arena():
    #get user input for drink name and recipe
    body = request.get_json()
    arena_name = body.get('name', None)
    print(arena_name)
    arena_address = body.get('address', None)
    print(arena_address)
    try:
      #insert the above data into the database and throw an error in case it fails
      arena = Arena(name = arena_name, address = arena_address)
      arena.insert()
    except:
      abort(422)
    
    return jsonify ({
        'success': True,
        'name': arena_name,
        'address':arena_address
    }), 200
    
  '''
  Select Arena
  '''
  @app.route('/arenas/<int:id>', methods=['GET'])
  def select_arena(id):
    arena = Arena.query.filter(Arena.id == id).first()

    if not arena:
      abort(404)

    return jsonify ({
      'success':True,
      'arena': arena.format()
      }), 200

  '''
  Add restaurant
  '''
  @app.route('/restaurants', methods=['POST'])
  def create_restaurant():
        
    try:
      body = request.get_json()
      restaurant_name = body.get('name', None)
      print(restaurant_name)
      restaurant_address = body.get('address', None)
      print(restaurant_address)
      arena_id = body.get('arena_id', None)
      print(arena_id)
    except:
      abort(422)

    #insert the above data into the database and throw an error in case it fails
    try:
      restaurant = Restaurant(name = restaurant_name, address = restaurant_address, arena_id = arena_id)
      restaurant.insert()
    except:
      abort(422)
        
    return jsonify ({
      'success': True,
      'name': restaurant_name
    }), 200

  '''
  View a list of all restaurants within an Arena
  '''
  @app.route('/arenas/<int:id>/restaurants', methods=['GET'])
  def get_restaurants_by_arena(id):
    #check if arena id is valid 
    if not id:
      abort(400)  

    #query for restaurants associated with the above arena id and store in restaurants variable
    restaurants = Restaurant.query.filter(Restaurant.arena_id == id)

    #loop through restaurants and list out each restaurant associated with the selected arena
    restaurant_list = [restaurant.format() for restaurant in restaurants]

    return jsonify ({
      'success': True,
      'restaurants':restaurant_list
    })
  
  '''
  Add new Menu to a restaurant
  '''
  @app.route('/menus/create', methods=['POST'])
  def add_menu():
    
    try:
      body = request.get_json()
      menu_name = body.get('name', None)
      print(menu_name)
      restaurant_id = body.get('restaurant_id', None)
      print(restaurant_id)
    except:
      abort(422)
    
    #insert the new record into the database
    try:
      menu = Menu(name = menu_name, restaurant_id = restaurant_id)
      menu.insert()
    except:
      abort(422)
    
    return jsonify ({
      'success':True,
      'menu':menu_name
    }), 200
    


  '''
  Get list of menus by restaurant
  '''
  @app.route('/restaurants/<int:id>/menus', methods=['GET'])
  def get_menus(id):
    #check for vaid id
    if not id:
      abort(404)
    
    #query the db for the menu associated with the restaurant & store in var
    menus = Menu.query.filter(Menu.restaurant_id == id)

    #store the retrieved menus in a list
    menu_list = [menu.format() for menu in menus]

    #return the results in json
    return jsonify ({
      'success':True,
      'menus':menu_list
    }), 200

  '''
  remove a menu within a restaurant
  '''
  @app.route('/menus/<int:menu_id>', methods=['DELETE'])
  def remove_menu(menu_id):
    #check for vaid id
    menu = Menu.query.filter(Menu.id == menu_id).one_or_none()
    if not id:
      abort(404)
    try:
      #delete the menu
      menu.delete()
    except:
      abort(422)

    #return the results in json
    return jsonify ({
      'success':True,
      'deleted_menu':menu_id
    }), 200

  '''
  Change menu name
  '''
  @app.route('/menus/<int:id>/edit', methods=['PATCH'])
  def edit_menu_name(id):
    #test to ensure valid id
    menu = Menu.query.get_or_404(id)

    #get updated menu name from user
    body = request.get_json()
    menu_name = body.get('name', None)
    print(menu_name)

    #update menu in db
    try:
      menu = Menu(name = menu_name)
      menu.update()
    except:
      abort(422)

    #return json
    return jsonify({
      'success':True,
      'menu_name':menu_name
    }), 200

  '''
  Add menu items to an existing menu
  '''

  '''
  Add a runner
  '''

  '''
  add a new customer
  '''




  # Error Handling
  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
                      "success": False, 
                      "error": 422,
                      "message": "unprocessable"
                      }), 422

  '''
  '''
  @app.errorhandler(404)
  def not_found(error):
      return jsonify({
                      "success": False, 
                      "error": 404,
                      "message": "Not Found"
                      }), 404
  '''
  '''
  @app.errorhandler(405)
  def method_not_allowed(error):
      return jsonify({
          'success': False,
          'error': 405,
          'message': 'method not allowed'
      }, 405)


  return app



APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)