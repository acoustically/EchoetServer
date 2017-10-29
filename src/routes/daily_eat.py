from flask import Blueprint, jsonify, request
from src.models.daily_eat import DailyEat
from src.models.food import Food
import src.orm as orm
import datetime
from src.db_connector import DBConnector

daily_eat = Blueprint("daily_eat", __name__)

connector = DBConnector()

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

@daily_eat.route("/all", methods=["POST"])
def get_all_by_day():
    json = request.get_json();
    print(json)
    user_id = json["user_id"]
    year = json["year"]
    month = json["month"]
    date = json["date"]
    
    sql = "select de.food_name, de.count, f.kcal, f.co2 from daily_eats as de, foods as f where de.user_id='%s' and de.food_name=f.name and de.year=%s and de.month=%s and de.date=%s;" % (user_id, year, month, date);
    print(sql)
    result, err = connector.query(sql);
    print(result)   
    return jsonify(daily_eats=result)

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
    
    for daily_eat in daily_eats:
        user_id = daily_eat["user_id"]
        food_name = daily_eat["food_name"]
        year = daily_eat["year"]
        month = daily_eat["month"]
        date = daily_eat["date"]
        print(user_id)
        print(food_name)
        print(year)
        print(month)
        print(date)
    
        sql = "select count from daily_eats where user_id='%s' and food_name='%s' and year='%s' and month='%s' and date='%s';" % (user_id, food_name, year, month, date)
        result, err = connector.query(sql) 
        print(result[0]["count"])
        print("============")
        if err:
            if err["errno"] == 1602:
                sql = "insert into daily_eats(user_id, food_name, year, month, date) values('%s', '%s', '%s', '%s', '%s');" % (user_id, food_name, year, month, date)
                result, err = connector.query(sql)
        else:
            print("testsesaastsat")
            sql = "update daily_eats set count='%s' where user_id='%s' and food_name='%s' and year='%s' and month='%s' and date='%s';" % ((result[0]["count"] + 1), user_id, food_name, year, month, date)
            result, err = connector.query(sql)

    return jsonify({"response":"success"})

            

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

@daily_eat.route("/total/<user_id>")
def total(user_id):
    time = datetime.datetime.now()
    sql = "select de.food_name, f.kcal, f.co2, de.count from daily_eats as de, foods as f where de.user_id='%s' and f.name=de.food_name;" % user_id; 
    results, err = connector.query(sql)
    kcal = 0
    co2 = 0
    for result in results:
        kcal += result["kcal"] * result["count"]
        co2 += result["co2"] * result["count"]
    return jsonify({"total_kcal":kcal, "total_tree":co2, "size":len(results)})
       








