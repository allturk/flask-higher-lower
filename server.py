from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def print_guess():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" height=300>'


def generate_number():
    return random.randint(0, 9)


generated_num = generate_number()
@app.route("/<int:number>")
def check_number(number):
    if generated_num>number:
        return '<h1 style="color:red">Too Low</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif generated_num<number:
        return '<h1 style="color:blue"> Too High</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return '<h1 style="color:green">Correct</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
if __name__ == "__main__":
    app.run(debug=True)
