from flask_wtf import Form
from flask import Flask
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_bootstrap import Bootstrap
from flask import render_template

class NameForm(Form):
	name = StringField("What's your name?", validators=[Required()])
	submit = SubmitField('Submit')

app = Flask(__name__)	
app.config['SECRET_KEY'] = 'An encrypted string'
bootstrap = Bootstrap(app)

@app.route('/', methods=['POST', 'GET'])
def index():
	name = None
	form = NameForm()
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
	return render_template('index_04.html', form=form, name=name)

if __name__ == '__main__':
	app.run(debug=True)
