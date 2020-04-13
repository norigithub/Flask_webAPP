from flask_blog import db
from datetime import datetime

class Entry(db.Model):
    __tablename__ == 'entries'
    id = db.Colmun(db.Integer, primary_key=True)
    title = db.Colmun(db.String(50), unique=True)
    text = db.Colmun(db.Text)
    created_at = db.Column(db.Datatime)

    def __init__(self, title=None, text=None):
        self.title = title
        self.text = text
        self.created_at = datatime.utcnow()
    
    def __repr__(self):
        return '<Entry id: () title: () text ()>'.format(self.id, self.title, self.text)