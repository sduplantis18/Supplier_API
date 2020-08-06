import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import setup_db, Arena, Restaurant, Customer, Shipment, Menu, Menu_Item, Order, Runner, db_drop_and_create_all

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
        'name': arena_name
    }), 200

  # Error Handling
  '''
  Example error handling for unprocessable entity
  '''
  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
                      "success": False, 
                      "error": 422,
                      "message": "unprocessable"
                      }), 422

  '''
  @TODO implement error handlers using the @app.errorhandler(error) decorator
      each error handler should return (with approprate messages):
              jsonify({
                      "success": False, 
                      "error": 404,
                      "message": "resource not found"
                      }), 404
  '''
  @app.errorhandler(404)
  def not_found(error):
      return jsonify({
                      "success": False, 
                      "error": 404,
                      "message": "Not Found"
                      }), 404
  '''
  @TODO implement error handler for 404
      error handler should conform to general task above 
  '''
  @app.errorhandler(405)
  def method_not_allowed(error):
      return jsonify({
          'success': False,
          'error': 405,
          'message': 'method not allowed'
      }, 405)



  return app

db_drop_and_create_all

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)