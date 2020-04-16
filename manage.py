from flask_blog.scripts.db import init_db, drop_db
from flask_blog import create_app
import sys

if __name__ == '__main__':
    arg = sys.argv[1]
    if arg == 'init':
        init_db(create_app())
    elif arg == 'drop':
        drop_db(create_app())
    else:
        print('Invalid command')