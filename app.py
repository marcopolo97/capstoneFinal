import os
from flask import Flask, request, abort, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db

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
def get_entrees():

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
@app.route('/desserts', methods=['GET'])
def get_desserts():
  
  desserts = Dessert.query.all()


  
  return render_template('pages/entrees.html', desserts=data), 200

# Route to add a new Entree
@app.route('/entrees', methods=['POST'])
def add_entree():


  return render_template('pages/entrees.html')

# Route to update a Entree
@app.route('/entrees/<int:id>',  methods=['PATCH'])
def update_entree():

  return render_template('pages/entrees.html')

# Route to delete a Entree
@app.route('/entrees/<int:id>',  methods=['DELETE'])
def delete_entree():

  return render_template('pages/entrees.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)