from flask import Flask, jsonify, request
from auth.views import auth_bp
from api.views import api_bp

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, to the world of Uktob.ai  !"

app.register_blueprint(auth_bp)
app.register_blueprint(api_bp)

if __name__ == "__main__":
	app.run()
