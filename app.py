from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

answers = {}

# create form for all the words in Story class
# get all the inputs and create answer dictionary
# run Story.generate(answer_dictionary) => returns string to display in html

@app.get("/")
def show_question():
    """create a form that asks for an answer for each word"""

    prompts = silly_story.prompts
    return render_template("questions.html", prompts = prompts)

@app.get("/story")
def get_answers():
    """get form input values and updates the answers dictionary"""

    result_story = silly_story.generate(request.args)
    print(request.args)
    return render_template("results.html", result_story = result_story)

# request.args RETURNS THIS:
# ?place=tokyo&noun=cat&verb=run&adjective=nice&plural_noun=dogs
# [('place', 'paris'), ('noun', 'mouse'), ('verb', 'eat'), ('adjective', 'nice'), ('plural_noun', 'cats')]