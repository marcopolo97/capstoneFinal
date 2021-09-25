import os
from flask import Flask, request, abort, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db
from auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

# # Models.

from models import *

@app.route('/')
def index():
  return render_template('pages/home.html'), 200

# Route to get Entrees 
@app.route('/entrees', methods=['GET'])
@requires_auth('get:entrees')
def get_entrees(payload):

  data = []

  entrees = Entree.query.all()

  for entree in entrees:
    data.append({
    'meat': entree.meat,
    'side_1': entree.side_1,
    'side_2': entree.side_2,
    'price': entree.price
  })

  print(data)

  return render_template('pages/entrees.html', entrees=data), 200

# Route to get Desserts
@app.route('/drinks', methods=['GET'])
@requires_auth('get:drinks')
def get_drinks():

  data = []

  drinks = Drink.query.all()

  for drink in drinks:
    data.append({
    'name': drink.name,
    'price': drink.price
  })

    print(data)

  
  return render_template('pages/drinks.html', drinks=data), 200

# Route to add a new Entree
@app.route('/entrees', methods=['POST'])
@requires_auth('post:entrees')
def add_entree():

  body = request.get_json()
  print(body)
  try: 
    
    
    new_meat = body.get('meat')
    new_side1 = body.get('side_1')
    new_side2 = body.get('side_2')
    new_price = body.get('price')

    entree = Entree(meat=new_meat, side_1=new_side1, side_2=new_side2, price=new_price)

    entree.insert()


    return jsonify({
      'success': True,
      'entree': entree
      }), 200

  except Exception as e:
    
    print('Exception is >> ', e)
    abort(422)

# Route to update a Entree
@app.route('/entrees/<int:id>',  methods=['PATCH'])
@requires_auth('update:entrees')
def update_entree(id):
  
  entree = Entree.query.filter(Entree.id == id).one_or_none()

  if not entree:
    
    abort(404)
    
  body = request.get_json()
  
  try:
    
    new_meat = body.get('meat')
    
    if new_meat:
      entree.meat = new_meat
      
    new_side1= body.get('side_1')
    
    if new_side1:
      entree.side_1 = new_side1

    new_side2= body.get('side_2')
    
    if new_side2:
      entree.side_2 = new_side2

    new_price= body.get('price')
    
    if new_price:
      entree.price = new_price

    entree.update()

    return jsonify({
      'success': True,
      #'entree': entree
      }), 200

  except Exception as e:
    
    print('Exception is >> ', e)
    abort(422)

# Route to delete a Entree
@app.route('/entrees/<int:id>',  methods=['DELETE'])
@requires_auth('delete:entrees')
def delete_entree(id):

  entree = Entree.query.filter(Entree.id == id).one_or_none()

  if not entree:
    
    abort(404)
    
  body = request.get_json()

  try:
    
    entree.delete()

    return jsonify({
        'success': True,
        'delete': id
    }), 200
    
  except Exception as e:
    
    print('Exception is >> ', e)
    abort(422)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)