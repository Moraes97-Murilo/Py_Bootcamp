from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Damned World!</p>"

@app.route("/wine")
def kanpai():
    return "<p>A very nice glass of wine, Cheers!</p>"

if __name__ == "__main__":
    app.run()