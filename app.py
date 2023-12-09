from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")
@app.route("/main")
def main():
    return render_template("main.html")
@app.route("/register")
def register():
    return render_template("register.html")
@app.route("/login")
def login():
    return render_template("login.html")

if __name__=="__main__":
    app.run(debug=True)
