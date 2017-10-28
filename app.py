from flask import Flask, request, jsonify
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
    return 

if  __name__ == "__main__":
    app.run(host="0.0.0.0")

