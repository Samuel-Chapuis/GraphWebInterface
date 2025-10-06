"""
Graph Analysis Module
=====================

This module provides functions to analyze directed graphs represented as adjacency matrices.
It tests various mathematical properties of graphs including completeness, reflexivity,
symmetry, antisymmetry, and transitivity.

Functions:
- build_adjacency_matrix: Constructs an adjacency matrix from points and links
- is_complete: Tests if all possible edges exist (except self-loops)
- is_reflexive: Tests if all vertices have self-loops
- is_symmetric: Tests if the relation is symmetric (a->b implies b->a)
- is_antisymmetric: Tests if the relation is antisymmetric (a->b and b->a implies a=b)
- is_transitive: Tests if the relation is transitive (a->b and b->c implies a->c)
- analyze_graph: Performs complete graph analysis

Author: Samuel Chapuis
Date: October 6, 2025
Version: 1.0
"""

def build_adjacency_matrix(points, links):
    """Construit la matrice d'adjacence à partir des points et liens"""
    n = len(points)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    id_to_index = {p['id']: i for i, p in enumerate(points)}
    
    for link in links:
        if link['from'] in id_to_index and link['to'] in id_to_index:
            i = id_to_index[link['from']]
            j = id_to_index[link['to']]
            matrix[i][j] = 1
    
    return matrix

def is_complete(matrix):
    """Test si le graphe est complet (toutes les arêtes possibles existent, sauf boucles)"""
    n = len(matrix)
    if n == 0:
        return False
    
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] != 1:
                return False
    return True

def is_reflexive(matrix):
    """Test si le graphe est réflexif (tous les sommets ont une boucle)"""
    n = len(matrix)
    if n == 0:
        return False
    
    for i in range(n):
        if matrix[i][i] != 1:
            return False
    return True

def is_symmetric(matrix):
    """Test si le graphe est symétrique (si a->b alors b->a)"""
    n = len(matrix)
    if n == 0:
        return False
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def is_antisymmetric(matrix):
    """Test si le graphe est antisymétrique (si a->b et b->a alors a=b)"""
    n = len(matrix)
    if n == 0:
        return False
    
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] == 1 and matrix[j][i] == 1:
                return False
    return True

def is_transitive(matrix):
    """Test si le graphe est transitif (si a->b et b->c alors a->c)"""
    n = len(matrix)
    if n == 0:
        return False
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if matrix[i][j] == 1 and matrix[j][k] == 1:
                    if matrix[i][k] != 1:
                        return False
    return True

def analyze_graph(points, links):
    """Analyse les propriétés du graphe"""
    n = len(points)
    if n == 0:
        return {
            'is_complete': False,
            'is_reflexive': False,
            'is_symmetric': False,
            'is_antisymmetric': False,
            'is_transitive': False,
            'num_vertices': 0,
            'num_edges': 0
        }
    
    matrix = build_adjacency_matrix(points, links)
    
    return {
        'is_complete': is_complete(matrix),
        'is_reflexive': is_reflexive(matrix),
        'is_symmetric': is_symmetric(matrix),
        'is_antisymmetric': is_antisymmetric(matrix),
        'is_transitive': is_transitive(matrix),
        'num_vertices': n,
        'num_edges': len(links)
    }
