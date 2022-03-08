from flask import flask

app = Flask(__name__)

@app.route("/home")
def home():
    return "Hello! this is Pluto page"<h1>HELLO</h1>

if __name__ == "__main__":
    app.run()