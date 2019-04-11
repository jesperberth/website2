from flask import Flask

app = Flask(__name__)

@app.route("/user/<username>")
def user(username):
    return "Hello World! %s " % username

@app.route("/product/")
def product():
    return "Product Site"

if __name__ == '__main__':
    app.run(debug=True)