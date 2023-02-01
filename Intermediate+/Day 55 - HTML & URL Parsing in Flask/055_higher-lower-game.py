from flask import Flask
from random import randint

random_number = randint(0, 9)
app = Flask(__name__)


def home_style(function):
    def wrapper():
        return f'<h1>{function()}</h1><img src="https://media3.giphy.com/media/qq7ef70oHLoAM/giphy.gif?cid' \
               f'=ecf05e4760j787uoe3in9hzegleooxi75giew1zjpe05bezo&rid=giphy.gif&ct=g">'
    return wrapper


@app.route("/")
@home_style
def home():
    return f"Guess a number between 0 and 9 <br>"


@app.route("/<int:guess>", endpoint='func1')
def too_low(guess):
    if guess < random_number:
        return '<h1>Too low!</h1>' \
               '<img src="https://media2.giphy.com/media/fnix5judzLJDJTaLgm/giphy.gif?cid' \
               '=790b7611e2881bbb1c09734447bb8740e05708df8b2414d5&rid=giphy.gif&ct=g"> '
    if guess > random_number:
        return '<h1>Too High!</h1>' \
               '<img src="https://media1.giphy.com/media/CvgezXSuQTMTC/giphy.gif?cid' \
               '=790b761103fd94ab86e553a8016f273249ffb20b2e6988d0&rid=giphy.gif&ct=g"> '
    else:
        return '<h1>Right number!</h1>' \
               '<img src="https://media2.giphy.com/media/j9iwmVGwK4U1y/giphy.gif?cid' \
               '=790b761118d53b6c603f6cc99cddd83a3705a7dc31783ea3&rid=giphy.gif&ct=g"> '


if __name__ == "__main__":
    app.run(debug=True)
