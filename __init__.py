from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from user_app.config import Config

app = Flask(__name__, instance_path=Config.PROJECT_ROOT)
app.config.from_object(Config)

db = SQLAlchemy(app)

from user_app.userview import user_routes
app.register_blueprint(user_routes, url_prefix="/user")

