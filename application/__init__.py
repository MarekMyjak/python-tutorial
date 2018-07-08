from flask import Flask


def create_app():
    app = Flask(__name__)

    from application.index import main
    app.register_blueprint(main)

    return app


from application.index import routes
