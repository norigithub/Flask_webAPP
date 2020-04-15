from flask_blog import create_app, db

def init_db():
    app = create_app()
    db.init_app(app)

    with app.app_context():
        db.create_all()

def drop_db():
    app = create_app()
    db.init_app(app)

    with app.app_context():
        db.drop_all()