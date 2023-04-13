from flask import Flask

app = Flask(__name__)

@app.route("/username")
def user_home():
    return "Hi, this page works to greet new users."

@app.route("/username/<name>/<int:age>")
def greet_user(name,age):
    return f"Hello, {name}, nice to meet you! You are {age} year old."

if __name__ == "__main__":
    app.run(debug=True)