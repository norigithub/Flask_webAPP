from flask_blog import app
from flask_blog.scripts.db import InitDB

if __name__ == '__main__':
    manager = InitDB()
    manager.run()