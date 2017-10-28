from flask import Blueprint, jsonify, request
from src.models.food import Food
from src.models.daily_eat import DailyEat
import src.orm as orm

food = Blueprint("food", __name__)

session = orm.session

@food.route("/")
def all():
    foods = session.query(Food).all()
    list_foods = orm.as_list_dict(foods)
    return jsonify(foods = list_foods)

@food.route("/<name>")
def get_food_by_name(name):
    foods = session.query(Food).filter_by(name=name).all()
    list_foods = orm.as_list_dict(foods)
    return jsonify(foods = list_foods)

@food.route("/<name>", methods=["DELETE"])
def delete_food_by_name(name):
    food = session.query(Food).filter_by(name=name).first()
    try:
        session.delete(food)
        session.commit()
        return jsonify({"response":"success"})
    except Exception as err:
        return jsonify({"response":"error", "error":str(err)})

@food.route("/new", methods=["POST"])
def new():
    name = request.form.get("name")
    kcal = request.form.get("kcal")
    co2 = request.form.get("co2")
    food = Food(name=name, kcal=kcal, co2=co2)
    try:
        session.add(food)
        session.commit()
        return jsonify({"response":"success"})
    except Exception as err:
        return jsonify({"response":"error", "message":str(err)})
  
@food.route("/daily-eat", methods=["POST"])
def daily_eat_foods():
    user_id = request.form.get("user_id")
    year = request.form.get("year")
    month = request.form.get("month")
    date = request.form.get("date")
    daily_eat_foods = session.query(Food, DailyEat).filter(DailyEat.food_name == Food.name).filter(DailyEat.user_id==user_id).all()
    return jsonify(daily_eat_foods = orm.as_list_dict_join(daily_eat_foods))


