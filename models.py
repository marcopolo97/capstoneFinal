from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
#migrate = Migrate()

# setup our database

def db_setup(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
    #migrate.init_app(app, db)


# Models.
#----------------------------------------------------------------------------#

class Entree(db.Model):
    __tablename__ = 'Entree'

    id = db.Column(db.Integer, primary_key=True)
    meat = db.Column(db.String(120))
    side_1 = db.Column(db.String(120))
    side_2 = db.Column(db.String(120))
    price = db.Column(db.String(120))
    

    def __repr__(self):
        return '<Entree {}>'.format(self.name)


class Dessert(db.Model):
    __tablename__ = 'Dessert'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    price = db.Column(db.String(120))

    def __repr__(self):
        return '<Dessert {}>'.format(self.name)
