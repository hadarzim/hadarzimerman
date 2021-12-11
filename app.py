from flask import Flask, redirect, url_for
from flask import render_template

app = Flask(__name__)


@app.route('/')
def homepage1():
    return redirect('/home')



@app.route("/home")
def home():
    return redirect(url_for('second'))


@app.route("/second")
def second():
    return 'hello 2'



if __name__ == '__main__':
    app.run(debug=True)