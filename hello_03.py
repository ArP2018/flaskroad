from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask import render_template

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
	return render_template('index_03.html')

@app.route('/user/<name>')
def user(name):
	return render_template('user_03.html', name=name)

@app.errorhandler(404)
def handle_error_404(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def handle_error_500(e):
	return render_template('500.html'), 500

if __name__	 == '__main__':
	app.run(debug=True)
