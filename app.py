from flask import Flask, render_template, request,flash,redirect
from flask_sqlalchemy import SQLAlchemy

app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SECRET_KEY']='thissecret'
db = SQLAlchemy(app)
app.app_context().push()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable=False)
    email = db.Column(db.String)
    password = db.Column(db.String, nullable=False)
    
    
def __repr__(self):
        return '<User %r>' % self.username
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/main")
def main():
    return render_template("main.html")
@app.route("/register",methods=['GET','POST'])
def register():
    if request.method=='POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        username = request.form.get('uname')
        # print(email,password,fname,lname,username,name)
        user=User(username=username,fname=fname,lname=lname,email=email,password=password)
        db.session.add(user)
        db.session.commit()
        flash('user has been registered successfully','success')
        return redirect('/login')

    return render_template("register.html")
@app.route("/login")
def login():
    return render_template("login.html")

if __name__=="__main__":
    app.run(debug=True)
