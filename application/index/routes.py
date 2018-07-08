from flask import render_template
from application.index import index


@index.route('/')
@index.route('/index')
def index():
    user = {'username': 'Marek'}
    return render_template('index.html', title='Home', user=user)
