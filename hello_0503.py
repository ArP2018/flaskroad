from flask import Flask, redirect, session, url_for, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
import os
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'an encrypted key'   # 防止跨域访问攻击
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'data.sqllite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

bootstrap = Bootstrap(app)
migrate = Migrate(app, db)
manager = Manager(app)

class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	users = db.relationship('User', backref='role', lazy='dynamic')

	def __repr__(self):
		return '<Role %s>'%self.name

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), unique=True, index=True)
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

class NameForm(FlaskForm):
	name = StringField('what is your name?', validators=[Required()])
	submit = SubmitField('submit')

@app.route('/', methods=['GET', 'POST'])	
def index():
    form = NameForm()
    if form.validate_on_submit():
    	user = User.query.filter_by(username=form.name.data).first()
    	if user is None:
    		user = User(username=form.name.data)
    		db.session.add(user)
    		db.session.commit()
    		session['known'] = False
    	else:
    		session['known'] = True
    	session['name'] = form.name.data
    	form.name.data = ''
    	return redirect(url_for('index'))
    return render_template('index_0502.html', form=form,
    	name=session.get('name'), known=session.get('known', False))

def make_shell_context():
	return dict(app=app, db=db, User=User, Role=Role)

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()
