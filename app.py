from flask import Flask, request, jsonify

app = Flask(__name__)

#TODO app.register_blueprint(user, url_prefix="/user")
if  __name__ == "__main__":
    app.run(host="0.0.0.0")

