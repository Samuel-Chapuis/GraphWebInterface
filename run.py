"""
Interactive Graph Application - Flask Backend
==============================================

This Flask application provides a backend for an interactive graph visualization tool.
Users can create points on a canvas and establish directed relationships between them.

Features:
- Add points with unique IDs and random colors
- Create directed links between points (including self-loops)
- Generate adjacency matrix representation
- Analyze graph properties (completeness, reflexivity, symmetry, etc.)
- Reset the graph to start over
- Fill the diagonal (add self-loops to all points)

Author: Samuel Chapuis
Date: October 6, 2025
Version: 1.0
"""


""" External imports """
from flask import Flask, request, jsonify, send_from_directory
import os
import numpy as np

""" Internal imports """
from analyze import (analyze_graph, build_adjacency_matrix)
from returner import (strict_relation, indiference_relation, topological_sort_soft, topological_sort_strict)


app = Flask(__name__)

# Store points: list of dicts {'id': str, 'x': float, 'y': float, 'color': str}
points = []
# Store links: list of dicts {'from': str, 'to': str}
links = []

def get_random_color():
    import random
    return f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}"

def get_next_id():
    if not points:
        return 'A'
    last_id = points[-1]['id']
    return chr(ord(last_id) + 1)


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/add_point', methods=['POST'])
def add_point():
    data = request.get_json()
    x = data.get('x')
    y = data.get('y')
    point_id = get_next_id()
    color = get_random_color()
    points.append({'id': point_id, 'x': x, 'y': y, 'color': color})
    return jsonify({'id': point_id, 'color': color})

@app.route('/add_link', methods=['POST'])
def add_link():
    data = request.get_json()
    from_id = data.get('from')
    to_id = data.get('to')
    if not any(l['from'] == from_id and l['to'] == to_id for l in links):
        links.append({'from': from_id, 'to': to_id})
    return jsonify({'success': True})

@app.route('/reset', methods=['POST'])
def reset_graph():
    global points, links
    points = []
    links = []
    return jsonify({'success': True})

@app.route('/fill_diagonal', methods=['POST'])
def fill_diagonal():
    for point in points:
        link = {'from': point['id'], 'to': point['id']}
        if not any(l['from'] == link['from'] and l['to'] == link['to'] for l in links):
            links.append(link)
    return jsonify({'success': True})

@app.route('/matrix')
def get_matrix():
    matrix = build_adjacency_matrix(points, links)
    analysis = analyze_graph(points, links)
    
    return jsonify({
        'matrix': matrix.tolist(), 
        'points': points, 
        'links': links,
        'analysis': analysis
    })

@app.route('/strict_relation')
def get_strict_relation():
    matrix = build_adjacency_matrix(points, links)
    strict = strict_relation(matrix)
    return jsonify({'matrix': strict.tolist()})

@app.route('/indifference_relation')
def get_indifference_relation():
    matrix = build_adjacency_matrix(points, links)
    indifference = indiference_relation(matrix)
    return jsonify({'matrix': indifference.tolist()})

@app.route('/topological_sort_soft')
def get_topological_sort_soft():
    matrix = build_adjacency_matrix(points, links)
    sort = topological_sort_soft(matrix)
    return jsonify({'sort': sort})

@app.route('/topological_sort_strict')
def get_topological_sort_strict():
    matrix = build_adjacency_matrix(points, links)
    sort = topological_sort_strict(matrix)
    return jsonify({'sort': sort})

if __name__ == '__main__':
    print("Starting Flask application...")
    print("Open your browser at: http://127.0.0.1:5000/")
    app.run(debug=True, host='0.0.0.0', port=5000)