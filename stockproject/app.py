from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_bootstrap import Bootstrap

from stockproject.blueprints.ui import ui
from stockproject.models import db, User

app = Flask(__name__)

# config
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.secret_key = 'foo'

# blueprints
app.register_blueprint(ui)

# setup database
db.init_app(app)
db.create_all(app=app)

# setup admin ui
admin = Admin(app, name='stockproject', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))

# setup bootstrap
bootstrap = Bootstrap(app)

app.run()

