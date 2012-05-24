#!/usr/bin/env python

import networkx as nx
import string
import sys

"""
dijkstra_path(G, start, end)
Calculate the minimum weighted path between two nodes for a NetworkX graph
---
Contact: Marshall Ward (marshall.ward@gmail.com)
"""
# TODO: Return the path, not the numbers :p
def dijkstra_path(G, start, end):
    unvisited = G.nodes()
    distance = {n: sys.maxint for n in unvisited}
    distance[start] = 0
    
    current = start
    while unvisited:
        neighbors = [n for n in G.neighbors(current) if n in unvisited]
        
        # Diagnostic
        print 'Current node:', current
        print 'Neighbors:', neighbors
        
        # Update distances
        for n in neighbors:
            local_dist = distance[current] + G[current][n]['weight']
            distance[n] = min(distance[n], local_dist)
            print 'Node:', n, 'Distance:', distance[n]
        
        # Remove the current node and determine the next node
        unvisited.remove(current)

        # Diagnostic
        print 'Unvisited:', unvisited
        print 'Distances:', distance

        # Search termination
        # TODO: Check for infinite distances
        try:
            current = min(neighbors, key=distance.get)
        except ValueError:
            print "done"
            break
    
    return distance

# Generate a sample NetworkX graph (from the Wikipedia example)
def create_sample_graph():

    node_list = range(6)
    edge_list = [(0, 1, 7),
                 (0, 2, 9),
                 (0, 5, 14),
                 (1, 2, 10),
                 (1, 3, 15),
                 (2, 3, 11),
                 (2, 5, 2),
                 (3, 4, 6),
                 (4, 5, 9)]
    
    G = nx.Graph()
    G.add_nodes_from(node_list)
    G.add_weighted_edges_from(edge_list)

    return G


def main():
    G = create_sample_graph()
    path = dijkstra_path(G, 0, 4)


if __name__ == '__main__':
    main()
