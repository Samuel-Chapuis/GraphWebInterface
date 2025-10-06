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

Author: Samuel Chapuis
Date: October 2, 2025
Version: 1.0
"""


""" External imports """
from flask import Flask, request, jsonify, send_from_directory
import os

""" Internal imports """
from analyze import (analyze_graph, build_adjacency_matrix)


app = Flask(__name__)

# Stocker les points : liste de dicts {'id': str, 'x': float, 'y': float, 'color': str}
points = []
# Stocker les liens : liste de dicts {'from': str, 'to': str}
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

@app.route('/matrix')
def get_matrix():
    matrix = build_adjacency_matrix(points, links)
    analysis = analyze_graph(points, links)
    
    return jsonify({
        'matrix': matrix, 
        'points': points, 
        'links': links,
        'analysis': analysis
    })

if __name__ == '__main__':
    print("Démarrage de l'application Flask...")
    print("Ouvrez votre navigateur à : http://127.0.0.1:5000/")
    app.run(debug=True, host='0.0.0.0', port=5000)