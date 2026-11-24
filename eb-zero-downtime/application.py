import os

from flask import Flask, jsonify, render_template

application = Flask(__name__)

APP_ENV = os.environ.get("APP_ENV", "development")
APP_MESSAGE = os.environ.get("APP_MESSAGE", "Welcome to Elastic Beanstalk")
APP_VERSION = os.environ.get("APP_VERSION", "1.0")

@application.route("/")
def home():
    return render_template(
        "index.html",
        message=APP_MESSAGE,
        environment=APP_ENV,
        version=APP_VERSION,
    )


@application.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000)
