from flask import Flask
from decorators import styling as make

app = Flask(__name__)

#Home message
default = "Hi, this page works to greet new users."
style = ['b','u','en','h1']

@make
def styling(x,y):
    pass

@app.route("/username")
def user_home():
    return default

@app.route("/username/<name>/<int:age>")
def greet_user(name,age):
    return f'<h1 style="text-align: center">Hello, {name}, nice to meet you! </h1> \
             <p>You are {age} year old.</p> \
             <img src="https://media1.giphy.com/media/sertChLDKT2ms/giphy.gif" width=200> ' 
             

if __name__ == "__main__":
    default = styling(style,default)
    app.run(debug=True)