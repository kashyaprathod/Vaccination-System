from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('index.html')


@app.route("/SignIn")
def sign_in():
    return render_template('signin.html')


@app.route("/Profile")
def profile():
    return render_template('profile.html')



