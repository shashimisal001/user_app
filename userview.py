from flask import Blueprint, request
from flask.views import MethodView
from user_app import db
from user_app.user import User
import hashlib as hl


user_routes = Blueprint("user_routes", __name__)


class UserView(MethodView):
    def get(self):
        username = request.args.get("username")
        password = request.args.get("password")
        enc_password = hl.md5(password.encode()).hexdigest()
        db_user = User.query.filter_by(username=username, password=enc_password).all()
        if db_user is not None:
            return str(db_user)
        else:
            return {}

    def post(self):
        data = request.get_json()
        username = data["username"]
        enc_password = hl.md5(data["password"].encode()).hexdigest()
        user = User(username=username, password=enc_password)
        db.session.add(user)
        db.session.commit()
        return dict({"msg": "User successfully created"})


user_obj = UserView()
user_routes.add_url_rule("", view_func=user_obj.get, methods=["GET"])
user_routes.add_url_rule("", view_func=user_obj.post, methods=["POST"])