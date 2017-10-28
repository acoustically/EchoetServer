from flask import Flask, request, jsonify, render_template
from src.routes.daily_eat import daily_eat
from src.routes.user import user
from src.routes.food import food
from src.routes.user_body import user_body

app = Flask(__name__)

app.register_blueprint(user, url_prefix="/user")
app.register_blueprint(daily_eat, url_prefix="/daily-eat")
app.register_blueprint(food, url_prefix="/food")
app.register_blueprint(user_body, url_prefix="/user-body")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user_list")
def user_list():
    return render_template("user_list.html")

@app.route("/user_comments")
def user_comments():
    return render_template("user_comments.html")

@app.route("/food_list")
def food_list():
    return render_template("food_list.html")



if  __name__ == "__main__":
    app.run(host="0.0.0.0")

