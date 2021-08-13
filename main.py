from flask import Flask, render_template

app = Flask(__name__)

'''
Jinja FILTERS
safe
capitalize
lower
upper
title
trim
striptags
'''


@app.route('/')
# def index():
#    return "<h1>Hello World</h1>"
def index():
    first_name = "Swapnil"
    stuff = "This is Bold text"

    favorite_pizza = ["Pepperoni", "Cheese", "Mushrooms", 41]
    return render_template("index.html", first_name=first_name, stuff=stuff, favorite_pizza=favorite_pizza)


@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)


# Invalid URL 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template("error404.html"), 404


# Internal Server Error 500
@app.errorhandler(500)
def page_not_found(e):
    return render_template("error500.html"), 500


app.run(debug=True)
