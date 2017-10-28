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
def get_daily_eat_by_user_id(user_id):
    daily_eats = session.query(DailyEat).filter_by(user_id=user_id).all()
    list_daily_eats = orm.as_list_dict(daily_eats)
    return jsonify(daily_eats = list_daily_eats)

@daily_eat.route("/delete", methods=["POST"])
def delete_daily_eat():
    user_id = request.form.get("user_id")
    food_name = request.form.get("food_name")
    year = request.form.get("year")
    month = request.form.get("month")
    date = request.form.get("date")
    
    try:
        daily_eat = session.query(DailyEat).filter_by(user_id=user_id, food_name=food_name, year=year, month=month, date=date).first()
        if daily_eat.count > 1:
            session.query(DailyEat).filter_by(user_id=user_id, food_name=food_name, year=year, month=month, date=date).update(dict(count=daily_eat.count - 1))
        else:
            daily_eat = session.query(DailyEat).filter_by(user_id=user_id, food_name=food_name, year=year, month=month, date=date).first()
            session.delete(daily_eat)
        session.commit()
        return jsonify({"response":"success"})
    except Exception as err:
        return jsonify({"response":"error", "error":str(err)})

@daily_eat.route("/new", methods=["POST"])
def new():
    user_id = request.form.get("user_id")
    food_name = request.form.get("food_name")
    year = request.form.get("year")
    month = request.form.get("month")
    date = request.form.get("date")
    if add(user_id, food_name, year, month, date):
        return jsonify({"response":"success"})
    else:
        return jsonify({"response":"error", "message":str(err)})

@daily_eat.route("/add", methods=["POST"])
def add_all():
    json = request.get_json()
    daily_eats = json["daily_eats"]
    print(daily_eats)
    is_success = True
    for daily_eat in daily_eats:
        print(daily_eat)
        is_success = is_success and add(daily_eat["user_id"], daily_eat["food_name"], daily_eat["year"], daily_eat["month"], daily_eat["date"])
    if is_success:
        return jsonify(daily_eats)
    else:
        for daily_eat in daily_eats:
            try:
                delete_data = session.query(DailyEat).filter_by(user_id=daily_eat["user_id"], food_name=daily_eat["food_name"], year=daily_eat["year"], month=daily_eat["month"], date=daily_eat["date"]).first()
                session.delete(delete_date)
            except Exception as err:
                print(str(err))
        return jsonify({"response":"error"})
            

def add(user_id, food_name, year, month, date):
    try:
        daily_eat = session.query(DailyEat).filter_by(user_id=user_id, food_name=food_name, year=year, month=month, date=date).first()
        if daily_eat.count > 0:
            daily_eat = session.query(DailyEat).filter_by(user_id=user_id, food_name=food_name, year=year, month=month, date=date).first()
            session.query(DailyEat).filter_by(user_id=user_id, food_name=food_name, year=year, month=month, date=date).update(dict(count=daily_eat.count + 1))
        else:
            daily_eat = DailyEat(user_id, food_name, year, month, date)
            session.add(daily_eat)
        session.commit()
        return True
    except Exception as err:
        return False

