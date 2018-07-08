from flask import render_template
from application.animals import animals


@animals.route('/animals')
def index():
    return render_template('animals.html', title='animals', friend='koteczek')
