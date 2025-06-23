from . import db

class Poll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), nullable=False)
    option1 = db.Column(db.String(100), nullable=False)
    option2 = db.Column(db.String(100), nullable=False)
    option3 = db.Column(db.String(100))
    option4 = db.Column(db.String(100))
    votes1 = db.Column(db.Integer, default=0)
    votes2 = db.Column(db.Integer, default=0)
    votes3 = db.Column(db.Integer, default=0)
    votes4 = db.Column(db.Integer, default=0)
