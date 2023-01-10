from flask import Flask
from app1.view import app1


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Development')
    app.register_blueprint(app1)
    return app


if __name__ == "__main__":
    create_app().run(debug=True)