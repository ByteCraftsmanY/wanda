from flask import Flask
from flask_cqlalchemy import CQLAlchemy
from flask_bcrypt import Bcrypt

from ..config import config_by_name

db = CQLAlchemy()
bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__)
    app_config = config_by_name.get(config_name)
    app.config.from_object(app_config)

    bcrypt.init_app(app)

    db.init_app(app)
    db.sync_db()
    return app
