from flask import render_template
from application.index import main


@main.route('/')
@main.route('/index')
def index():
    user = {'username': 'Marek'}
    return render_template('index.html', title='Home', user=user)
