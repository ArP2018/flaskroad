from flask.ext.bootstrap import Bootstrap
from flask import Flask
from flask import render_template
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/user/<name>')
def user(name):
	return render_template('user_02.html', name=name)

if __name__ == '__main__':
	app.run(debug=True)