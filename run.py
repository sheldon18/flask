import os
from flask import Flask, render_template     # captial F indicates that its a class name

app = Flask(__name__)       #in Flask, convention is that our variable is called app

@app.route("/")             #decorator, alwasy starts with an @ sign and aka pie notation, it is a way of wrapping functions
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html", page_title="About")
    
@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")
    
@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")      
    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)