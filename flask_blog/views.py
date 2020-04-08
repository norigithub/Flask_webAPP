from flask_blog import app

@app.route('/')
def show_etnries():
    return 'Hello World!'