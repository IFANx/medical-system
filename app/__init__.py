import os
from flask import Flask


def create_app(test_config=None):
    # create and config the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(app.instance_path, 'medical.db'),
        SQLALCHEMY_DATABASE_URI='mysql://medical:develop@127.0.0.1:3306/medical',  # mariadb uri
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ECHO=True,
    )

    if test_config is None:
        # load the instance config, if exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # initialize app with database
    from app.database import init_app
    init_app(app)

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'

    # register api
    from app.resources import doctors
    from app.resources import hospitals
    app.register_blueprint(doctors.bp)
    app.register_blueprint(hospitals.bp)

    return app
