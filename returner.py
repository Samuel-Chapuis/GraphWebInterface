"""
Graph Returnuer Module
=====================

This module provides functions returning graph properties. 

Functions:
- strict_relation: Returns the asymetric part of the matrix
- indiference_relation: Returns the symmetric part of the matrix
- topological_sort_soft: Returns a topological sort of the graph without cycles and the indifference pairwise comparisons
- topological_sort_strict: Returns a topological sort of the graph where the different pairwise comparisons exist

Author: Samuel Chapuis
Date: October 6, 2025
Version: 1.0
"""

import numpy as np

def strict_relation(matrix):
    """Returns the strict relation (asymmetric part) of the graph"""
    if matrix is None:
        return None
    # accept lists or numpy arrays
    mat = np.array(matrix, dtype=int)
    n = mat.shape[0]
    strict = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            if mat[i, j] == 1 and mat[j, i] == 0:
                strict[i, j] = 1
    return strict

def indiference_relation(matrix):
    """Returns the indiference relation (symmetric part) of the graph"""
    if matrix is None:
        return None
    # accept lists or numpy arrays
    mat = np.array(matrix, dtype=int)
    n = mat.shape[0]
    indiference = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            if mat[i, j] == 1 and mat[j, i] == 1:
                indiference[i, j] = 1
    return indiference

def topological_sort_soft(matrix):
    """Returns a topological sort of the graph without cycles and the indifference pairwise comparisons"""
    
    if matrix is None:
        return None
    mat = np.array(indiference_relation(matrix), dtype=int)
    if not np.all(mat == 0):
        print("Graph contains cycles or is empty")
        return []
    
    mat = np.array(matrix, dtype=int)
    n = mat.shape[0]
    strict = strict_relation(mat)

    # Build adjacency list ignoring indifference relations
    adj = {i: [] for i in range(n)}
    in_degree = [0] * n
    for i in range(n):
        for j in range(n):
            if strict[i, j] == 1:
                adj[i].append(j)
                in_degree[j] += 1

    # Kahn's algorithm for topological sort
    queue = [i for i in range(n) if in_degree[i] == 0]
    sorted_list = []

    while queue:
        node = queue.pop(0)
        sorted_list.append(node)
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(sorted_list) != n:
        return None  # Cycle detected

    return sorted_list
    


def topological_sort_strict(matrix):
    """Returns a topological sort of the graph where the different pairwise comparisons exist"""
    if matrix is None:
        return None
    mat = np.array(matrix, dtype=int)
    n = mat.shape[0]
    
    # Create a list to store the sorted elements
    sorted_list = []
    # Create a set to track visited nodes
    visited = set()
    
    def visit(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in range(n):
            if mat[node, neighbor] == 1 and mat[neighbor, node] == 0:
                visit(neighbor)
        sorted_list.append(node)
    
    for i in range(n):
        visit(i)
    
    sorted_list.reverse()
    
    return sorted_list
