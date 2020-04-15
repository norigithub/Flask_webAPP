from flask_blog.scripts.db import init_db, drop_db
import sys

if __name__ == '__main__':
    arg = sys.argv[1]
    if arg == 'init':
        init_db()
    elif arg == 'drop':
        drop_db()
    else:
        print('Invalid command')