from flask import Blueprint, jsonify, request
from src.models.user import User
import src.orm as orm

user = Blueprint("user", __name__)

session = orm.session

@user.route("/")
def all():
    users = session.query(User).all()
    list_users = orm.as_list_dict(users)
    print(list_users)
    return jsonify(users = list_users)

@user.route("/<id>")
def get_user_by_id(id):
    users = session.query(User).filter_by(id=id).all()
    list_users = orm.as_list_dict(users)
    return jsonify(users = list_users)

@user.route("/<id>", methods=["DELETE"])
def delete_user(id):
    user = session.query(User).filter_by(id=id).first()
    number_of_user = session.query(User).filter_by(id=id).count()
    try:
        session.delete(user)
        session.commit()
        return jsonify({"response":"success"})
    except Exception as err:
        return jsonify({"response":"error", "error":str(err)})

@user.route("/new", methods=["POST"])
def new():
    id = request.form.get("id")
    password = request.form.get("password")
    print(password)
    user = User(id=id, password=password)
    try:
        session.add(user)
        session.commit()
        return jsonify({"response":"success"})
    except Exception as err:
        return jsonify({"response":"error", "message":str(err)})
   
