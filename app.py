from flask import Flask
app =Flask(__name__)

@app.route("/")
def index():
    return("Home page")
@app.route("/register")
def register():
    return("Register page")
@app.route("/login")
def login():
    return("login page")

if __name__=="__main__":
    app.run(debug=True)
