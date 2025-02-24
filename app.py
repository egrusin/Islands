from flask import Flask, render_template, request, jsonify
from island import count_islands, generate_random_grid

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')