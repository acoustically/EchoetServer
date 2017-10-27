from flask import Flask, request, jsonify
from src.routes.daily_eat import daily_eat

app = Flask(__name__)

app.register_blueprint(daily_eat, url_prefix="/daily-eat")

if  __name__ == "__main__":
    app.run(host="0.0.0.0")

