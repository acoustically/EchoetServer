from flask import Blueprint, jsonify, request
from src.models.daily_eat import DailyEat
import src.orm as orm

daily_eat = Blueprint("daily_eat", __name__)

session = orm.session
@daily_eat.route("/")
def all():
    daily_eats = session.query(DailyEat).all()
    list_daily_eats = orm.as_list_dict(daily_eats)
    return jsonify(daily_eats = list_daily_eats)

@daily_eat.route("/<user_id>")
def get_user_daily_eat(user_id):
    daily_eats = session.query(DailyEat).filter_by(user_id=user_id).all()
    list_daily_eats = orm.as_list_dict(daily_eats)
    return jsonify(daily_eats = list_daily_eats)

@daily_eat.route("/delete", methods=["POST"])
def delete_user_daily_eat():
    user_id = request.form.get("user_id")
    food = request.form.get("food")
    year = request.form.get("year")
    month = request.form.get("month")
    date = request.form.get("date")
    
    daily_eat = session.query(DailyEat).filter_by(user_id=user_id, food=food, year=year, month=month, date=date).first()
    number_of_daily_eat = session.query(DailyEat).filter_by(user_id=user_id, food=food, year=year, month=month, date=date).count()
    if number_of_daily_eat == 0:
        return jsonify({"response":"error", "message":"that daily eat not exist"})
    try:
        if daily_eat.count > 1:
            session.query(DailyEat).filter_by(user_id=user_id, food=food, year=year, month=month, date=date).update(dict(count=daily_eat.count - 1))
        else:
            daily_eat = session.query(DailyEat).filter_by(user_id=user_id, food=food, year=year, month=month, date=date).first()
            session.delete(daily_eat)
        session.commit()
        return jsonify({"response":"success"})
    except Exception as err:
        return jsonify({"response":"error", "error":str(err)})

@daily_eat.route("/new", methods=["POST"])
def new():
    user_id = request.form.get("user_id")
    food = request.form.get("food")
    year = request.form.get("year")
    month = request.form.get("month")
    date = request.form.get("date")
    number_of_daily_eat = session.query(DailyEat).filter_by(user_id=user_id, food=food, year=year, month=month, date=date).count()
    try:
        if number_of_daily_eat > 0:
            daily_eat = session.query(DailyEat).filter_by(user_id=user_id, food=food, year=year, month=month, date=date).first()
            session.query(DailyEat).filter_by(user_id=user_id, food=food, year=year, month=month, date=date).update(dict(count=daily_eat.count + 1))
        else:
            daily_eat = DailyEat(user_id, food, year, month, date)
            session.add(daily_eat)
        session.commit()
        return jsonify({"response":"success"})
    except Exception as err:
        return jsonify({"response":"error", "message":err[0]})
   
