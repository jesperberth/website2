from flask import Flask

app = Flask(__name__)

@app.route("/user/<username>")
def hello(username):
    return "Hello World! %s " % username


if __name__ == '__main__':
    app.run(debug=True)