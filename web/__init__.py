from flask import Flask, render_template

app = Flask(__name__, template_folder='static/templates')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/board', methods=['GET'])
def board():
    return render_template('svgs/board.svg')
