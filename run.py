import os
from flask import Flask     # captial F indicates that its a class name

app = Flask(__name__)       #in Flask, convention is that our variable is called app

@app.route("/")             #decorator, alwasy starts with an @ sign and aka pie notation, it is a way of wrapping functions
def index():
    return "Hello, World"
    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)