from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

database_path = 'postgres://dmwtwcdoxxzbld:21a94858af4e2cf3104d175df8ab11d1f769f04e75ec23d13505eb9055a2cd98@ec2-44-199-83-229.compute-1.amazonaws.com:5432/d315l9hb4191lk'

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


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
