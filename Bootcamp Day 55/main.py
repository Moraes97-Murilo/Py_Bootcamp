from flask import Flask

app = Flask(__name__)

@app.route("/username")
def user_home():
    return "Hi, this page works to greet new users."

@app.route("/username/<name>")
def greet_user(name):
    return f"Hello, {name}, nice to meet you!"

if __name__ == "__main__":
    app.run()