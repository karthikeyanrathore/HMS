import os

from flask import Flask
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'iq.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def hello():
        return render_template('index.html')

    from . import db
    db.init_app(app)

    from . import patient
    app.register_blueprint(patient.bp)

    from . import doctor
    app.register_blueprint(doctor.bp)

    from . import department
    app.register_blueprint(department.bp)


    from . import nurse
    app.register_blueprint(nurse.bp)

    from . import wards
    app.register_blueprint(wards.bp)

    from . import treatment
    app.register_blueprint(treatment.bp)

	

    return app
