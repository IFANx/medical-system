import os
from flask import Flask


def create_app(test_config=None):
    # create and config the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(app.instance_path, 'medical.db'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ECHO=True,
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # initialize app with database
    from app.database import init_app
    init_app(app)

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, world!'

    # register api
    from app.resources import doctors
    from app.resources import hospitals
    app.register_blueprint(doctors.bp)
    app.register_blueprint(hospitals.bp)

    app.after_request(cors)

    return app


def cors(res):
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res
