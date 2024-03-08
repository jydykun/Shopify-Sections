from flask import Flask


def create_app():

    app = Flask(__name__)
    app.config["SECRET_KEY"] = "dev"

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    return app

