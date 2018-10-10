from . import db


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(64))
    press = db.Column(db.String(64))
    title_name = db.Column(db.String(128))
    title_link = db.Column(db.String)
    body = db.Column(db.String)

