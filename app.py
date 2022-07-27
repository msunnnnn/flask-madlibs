from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


# create form for all the words in Story class
# get all the inputs and create answer dictionary
# run Story.generate(answer_dictionary) => returns string to display in html

@app.get("/questions")
def show_question():
    """create a form that asks for an answer for each word"""
    prompts = silly_story.prompts
    return render_template("questions.html", prompts = prompts)
