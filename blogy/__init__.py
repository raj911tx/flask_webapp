import os
from flask import Flask
from . import db
from . import auth

def create_app(test_config=None):
    #it is a application factory function
    #creating app and configuring it
    app=Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path,'blogy.sqlite')
    )

    if test_config is None:
        #loads the instance configuration
        app.config.from_pyfile('config.py',silent=True)
    else:
        #loads it if passed in function parameter
        app.config.from_mapping(test_config)

    try:
        #check if instance folder exists
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return 'Hello World'

    db.init_app(app)
    app.register_blueprint(auth.bp)

    return app