from flask import Flask, redirect, url_for
import random

app = Flask(__name__)

guess_numb = 0

def change_numb():
    global guess_numb
    new_numb = random.randint(1, 9)
    while new_numb == guess_numb:
       new_numb = random.randint(1, 9)
    guess_numb = new_numb


@app.route('/')
def index():
    change_numb()
    return ('<div style="text-align: center"><h1>Guess a number 1-9 </h1>'
            '<p style="font-size: 20px">Put your guess in the address bar with<strong>&nbsp; < /(your guess)<?u></strong></p>'
            '<img src="https://i.redd.it/8vhs36c6d3o51.jpg" style="width:300px" />'
            # f'<p>{guess_numb}</p>'
            '</div>')

@app.route('/<int:numb>')
def number_guess(numb):
    if numb == guess_numb:
        return (f'<div style="text-align: center">'
                f'<h1>You got it!</h1>'
                f'<img src="https://64.media.tumblr.com/705ea963e93e60c58c4027576479bedb/tumblr_nlhf3cMyK61svecmko1_500.gif" />'
                f'<br><button style="margin-top: 25px; padding: 15px; border-radius: 10px; background-color: green; color: white; font-size: 25px" '
                f'onclick="window.location.href=\'/change\'">Play again.</button>'
                f'</div>')
    elif numb > guess_numb:
        return (f'<div style="text-align: center"><h3>Your guess was {numb}</h3>'
                f'<h1>Sorry that is not the right number. Guess again.</h1>'
                f'<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExaWY1Ymphb2czOXhscm93dHcyNnJhNmt3emRpZmZ6eXN0ZGRuMXluNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/EfEFcSNKrH70c/giphy.webp"/>'
                f'<h3>Hint: {numb} is too big. Make a lower guess.</h3>'
                f'</div>')
    elif numb < guess_numb:
        return (f'<div style="text-align: center"><h3>Your guess was {numb}</h3>'
                f'<h1>Sorry that is not the right number. Guess again.</h1>'
                f'<img src="https://c.tenor.com/zIy_kVnRYLMAAAAC/cat-shake.gif"/>'
                f'<h3>Hint: {numb} is too small. Make a higher guess.</h3>'
                f'</div>')

@app.route('/change')
def change_number_route():
    change_numb()
    return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(debug=True)