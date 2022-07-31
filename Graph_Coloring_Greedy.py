# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 09:58:05 2022

@author: Timur
"""
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations
import random

color_map = []

# A class to represent a graph object
class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
 
        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
 
# Function to assign colors to vertices of a graph
def colorGraph(graph, n):
 
    # keep track of the color assigned to each vertex
    result = {}; 
 
    # assign a color to vertex one by one
    for u in range(n):
 
        # check colors of adjacent vertices of `u` and store them in a set
        assigned = set([result.get(i) for i in graph.adjList[u] if i in result])
 
        # check for the first free color
        color = 1
        for c in assigned:
            if color != c:
                break
            color = color + 1
 
        # assign vertex `u` the first available color
        result[u] = color
        color_map.append(colors[result[u]])
  
    return result, color_map

    for v in range(n):

        print(f'Color assigned to vertex {v} is {colors[result[v]]}')


# Greedy coloring of a graph
 
# Add more colors for graphs with many more vertices
colors = ['', 'BLUE', 'GREEN', 'RED', 'YELLOW', 'ORANGE', 'PINK',
        'BLACK', 'BROWN', 'WHITE', 'PURPLE', 'VOILET']


####PARAMETERS##################
p = .4
n = 10
####PARAMETERS##################

V = set([v for v in range(n)])
edges = set()

control = -1
for combination in combinations(V, 2): 
    if combination[0] != control:
        edges.add(combination)
        control = combination[0]
    else:
        a = random.uniform(0, 1)
        if a < p:
            edges.add(combination)
    
G=nx.Graph(edges)


    
# build a graph from the given edges
graph = Graph(edges, n)

# color graph using the greedy algorithm
result, color_map = colorGraph(graph, n)

plt.title('Graph Coloring - Greedy Algorithm')
txt = ('Num of Color = ',  max(result.values()));
plt.text(0,-1.2,txt)
plt.text(0.4,-1.2,max(result))
nx.draw(G, node_color=color_map, with_labels=True)




plt.show()

    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    