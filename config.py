import os


class Config:
    PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(PROJECT_ROOT, 'user_app.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "secret"
