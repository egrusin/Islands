from flask import Flask, render_template, request, jsonify
from island import count_islands, generate_random_grid

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process_grid():
    data = request.get_json()
    rows = int(data['rows'])
    cols = int(data['cols'])
    grid = data.get('grid') or generate_random_grid(rows, cols)
    
    island_count, island_map = count_islands(grid)
    return jsonify({
        'grid': grid,
        'island_count': island_count,
        'island_map': island_map
    })


if __name__ == '__main__':
    app.run()