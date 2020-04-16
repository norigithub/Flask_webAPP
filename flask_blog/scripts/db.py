from flask_blog import db

def init_db(app):
    db.init_app(app)

    with app.app_context():
        db.create_all()

def drop_db(app):
    with app.app_context():
        db.drop_all()