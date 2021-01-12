from flask import Blueprint, render_template

ui = Blueprint('ui', __name__,  url_prefix='/', template_folder='templates')


@ui.route('/')
def hello_world():
    return render_template('index.html', data=[
        {
            'symbol': 'MSFT',
            'name': 'Microsoft',
            'change_percent': 12.0,
            'price': 50.0
        }
    ])


@ui.route('/register')
def register():
    return "Register"


@ui.route('/login')
def login():
    return "Login"
