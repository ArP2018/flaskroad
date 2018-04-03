from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, redirect, url_for, session
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'an encrpyted key'
bootstrap = Bootstrap(app)

class NameForm(FlaskForm):
	name = StringField('what is your name?', validators=[Required()])
	submit = SubmitField('submit')

@app.route('/', methods=['GET', 'POST'])	
def index():
	form = NameForm()
	if form.validate_on_submit():
		session['name'] = form.name.data
		return redirect(url_for('index'))
	return render_template('index_05.html', form=form, name=session.get('name'))

if __name__ == '__main__':
	app.run(debug=True)