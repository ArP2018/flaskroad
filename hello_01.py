from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/user/<name>')	
def user(name):
	return render_template('user.html', name=name, feature='handsome', friends=['Lucy', 'Lily', 'David'])

if __name__ == '__main__':
	app.run(debug=True)