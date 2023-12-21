from flask import Flask
from flask_migrate import Migrate

from blueprints import api_bp, genel_bp
from veri import *


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://eticaret_user:123456@localhost:5432/eticaret"
    migrate = Migrate()
    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/')
    def index():
        return {"sunucu": "ok"}
    app.register_blueprint(api_bp, url_prefix='/api')
    return app