from flask import Blueprint

main = Blueprint('index', __name__, template_folder='templates')

from app.index import routes
