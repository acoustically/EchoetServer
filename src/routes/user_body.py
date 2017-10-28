from flask import Blueprint, jsonify, request
from src.models.user_body import UserBody
import src.orm as orm

user_body = Blueprint("user_body", __name__)

session = orm.session

@user_body.route("/")
def all():
    bodys = session.query(UserBody).all()
    list_bodys = orm.as_list_dict(bodys)
    print(list_bodys)
    return jsonify(user_bodys = list_bodys)

@user_body.route("/<user_id>")
def get_user_bodys_by_user_id(user_id):
    bodys = session.query(UserBody).filter_by(user_id=user_id).all()
    list_bodys = orm.as_list_dict(bodys)
    return jsonify(user_bodys = list_bodys)

@user_body.route("/delete", methods=["POST"])
def delete_user_bodys():
    user_id = request.form.get("user_id")
    year = request.form.get("year")
    month = request.form.get("month")
    body = session.query(UserBody).filter_by(user_id=user_id, year=year, month=month).first()
    try:
        session.delete(body)
        session.commit()
        return jsonify({"response":"success"})
    except Exception as err:
        return jsonify({"response":"error", "error":str(err)})

@user_body.route("/new", methods=["POST"])
def new():
    user_id = request.form.get("user_id")
    year = request.form.get("year")
    month = request.form.get("month")
    weight = request.form.get("weight")
    height = request.form.get("height")
    body = UserBody(user_id=user_id, year=year, month=month, weight=weight, height=height)
    try:
        session.add(body)
        session.commit()
        return jsonify({"response":"success"})
    except Exception as err:
        return jsonify({"response":"error", "message":str(err)})
   
