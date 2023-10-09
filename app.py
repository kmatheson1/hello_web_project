import os
from flask import Flask, request
import pytest

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# Create a new route that responds to requests sent with:

# A method POST
# A path /submit
# Body parameters name and message

@app.route('/submit', methods=['POST'])
def submit_message():
    name = request.form['name']
    message = request.form['message']

    return f'Thanks {name}, you sent this message: "{message}"'

# Create a new route that responds to requests sent with:

# A method GET
# A path /wave
# A query parameter name

@app.route('/wave', methods=['GET'])
def wave():
    name = request.args['name']

    return f'I am waving at {name}'


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

# Test Driving Routes Exercise

@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    text = request.form['text']
    count = sum(1 for letter in text if letter in 'aeiou')
    return f'There are {count} vowels in "{text}"'

@app.route('/sort-names', methods=['POST'])
def post_sort_names():
    if 'names' not in request.form:
        return "You didn't submit any names!", 400
    names = request.form['names'].split(',')
    sorted_names = sorted(names)
    return ', '.join(sorted_names)


# Test Driving Routes Challenge

@app.route('/names', methods=['GET'])
def get_names():
    if 'add' not in request.args:
        return "No name provided", 400
    names = ['James', 'Leo']
    add = request.args['add'].split(',')
    for name in add:
        names.append(name)
    sorted_names = sorted(names)
    return ', '.join(sorted_names)