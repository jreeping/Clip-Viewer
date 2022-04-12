from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/clips")
def clips():
    return "Clips will Display Here!"

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/signup")
def login():
    return render_template('signup.html')

if __name__ == "__main__":
    app.run()