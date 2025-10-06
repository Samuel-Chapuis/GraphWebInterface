"""
Graph Analysis Module
=====================

This module provides functions to analyze directed graphs represented as adjacency matrices.
It tests various mathematical properties of graphs including strict completeness, soft completeness,
reflexivity, symmetry, antisymmetry, and transitivity.

Functions:
- build_adjacency_matrix: Constructs an adjacency matrix from points and links
- is_strictly_complete: Tests if all possible edges exist (except self-loops)
- is_soft_complete: Tests if at least one directed edge exists between every pair of distinct vertices
- is_reflexive: Tests if all vertices have self-loops
- is_symmetric: Tests if the relation is symmetric (a->b implies b->a)
- is_antisymmetric: Tests if the relation is antisymmetric (a->b and b->a implies a=b)
- is_transitive: Tests if the relation is transitive (a->b and b->c implies a->c)
- analyze_graph: Performs complete graph analysis

Author: Samuel Chapuis
Date: October 6, 2025
Version: 1.0
"""

import numpy as np

def build_adjacency_matrix(points, links):
    """Builds the adjacency matrix from points and links"""
    n = len(points)
    matrix = np.zeros((n, n), dtype=int)
    id_to_index = {p['id']: i for i, p in enumerate(points)}
    
    for link in links:
        if link['from'] in id_to_index and link['to'] in id_to_index:
            i = id_to_index[link['from']]
            j = id_to_index[link['to']]
            matrix[i, j] = 1
    
    return matrix

def is_complete(matrix):
    """Tests if the graph is complete (all possible edges exist, including self-loops)"""
    if matrix is None:
        return False
    n = matrix.shape[0]
    if n == 0:
        return False
    
    for i in range(n):
        for j in range(n):
            if matrix[i, j] == 0 and matrix[j, i] == 0:
                return False
    return True

def is_soft_complete(matrix):
    """Tests if the graph is soft complete (at least one directed edge exists between every pair of distinct vertices)"""
    if matrix is None:
        return False
    n = matrix.shape[0]
    if n == 0:
        return False
    
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i, j] == 0 and matrix[j, i] == 0:
                return False
    return True

def is_reflexive(matrix):
    """Tests if the graph is reflexive (all vertices have self-loops)"""
    if matrix is None:
        return False
    n = matrix.shape[0]
    if n == 0:
        return False
    
    for i in range(n):
        if matrix[i, i] != 1:
            return False
    return True

def is_symmetric(matrix):
    """Tests if the graph is symmetric (if a->b then b->a)"""
    if matrix is None:
        return False
    n = matrix.shape[0]
    if n == 0:
        return False
    
    for i in range(n):
        for j in range(n):
            if matrix[i, j] != matrix[j, i]:
                return False
    return True

def is_antisymmetric(matrix):
    """Tests if the graph is antisymmetric (if a->b and b->a then a=b)"""
    if matrix is None:
        return False
    n = matrix.shape[0]
    if n == 0:
        return False
    
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i, j] == 1 and matrix[j, i] == 1:
                return False
    return True

def is_transitive(matrix):
    """Tests if the graph is transitive (if a->b and b->c then a->c)"""
    if matrix is None:
        return False
    n = matrix.shape[0]
    if n < 3:  # Transitivity is not defined for graphs with less than 3 vertices
        return False
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if matrix[i, j] == 1 and matrix[j, k] == 1:
                    if matrix[i, k] != 1:
                        return False
    return True

def is_negatively_transitive(matrix):
    """Tests if the graph is negatively transitive (if not a->b and not b->c then not a->c)"""
    if matrix is None:
        return False
    n = matrix.shape[0]
    if n < 3:  # Negative transitivity is not defined for graphs with less than 3 vertices
        return False
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if matrix[i, j] == 0 and matrix[j, k] == 0:
                    if matrix[i, k] != 0:
                        return False
    return True

def is_complete_order(matrix):
    """Tests if the graph is a complete order (reflexive, antisymmetric, transitive, and complete)"""
    return (is_complete(matrix) and
            is_reflexive(matrix) and
            is_antisymmetric(matrix) and
            is_transitive(matrix))

def is_complete_preorder(matrix):
    """Tests if the graph is a complete preorder (reflexive, antisymmetric, transitive, and complete)"""
    return (is_complete(matrix) and
            is_transitive(matrix))



def analyze_graph(points, links):
    """Analyzes the graph properties"""
    n = len(points)
    if n == 0:
        return {
            'is_strictly_complete': False,
            'is_soft_complete': False,
            'is_reflexive': False,
            'is_symmetric': False,
            'is_antisymmetric': False,
            'is_transitive': False,
            'num_vertices': 0,
            'num_edges': 0,
            'is_complete_order': False,
            'is_complete_preorder': False
        }
    
    matrix = build_adjacency_matrix(points, links)
    
    return {
        'is_strictly_complete': is_complete(matrix),
        'is_soft_complete': is_soft_complete(matrix),
        'is_reflexive': is_reflexive(matrix),
        'is_symmetric': is_symmetric(matrix),
        'is_antisymmetric': is_antisymmetric(matrix),
        'is_transitive': is_transitive(matrix),
        'num_vertices': n,
        'num_edges': len(links),
        'is_complete_order': is_complete_order(matrix),
        'is_complete_preorder': is_complete_preorder(matrix)
    }
