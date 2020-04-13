from flask_blog import db

class InitDB():
    """Create database."""
    def run(self):
        db.create_all()