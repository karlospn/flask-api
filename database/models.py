import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


class Items(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String)
    quantity = db.Column(db.Integer)
