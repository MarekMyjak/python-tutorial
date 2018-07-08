from flask import Flask


def create_app():
    app = Flask(__name__)

    from application.index import index
    app.register_blueprint(index)

    from application.new_module import new_module
    app.register_blueprint(new_module)

    from application.animals import animals
    app.register_blueprint(animals)

    return app


from application.index import routes
