# %%
import sys
import networkx as nx
from matplotlib import pyplot as plt
import numpy as np
import json

# %%

import cascadeflr as cas


def new_network(n, k):
    """

    Create 2 random/binomial/Erdős-Rényi graph and a unified fully connected graph.

    Parameters
        - int n : number of nodes in
        - int k : edge creation coefficient

    Return
        - Graph G :
        - Graph g1 :
        - Graph g2 :

    """

    # create 2 random/binomial/Erdős-Rényi graph.
    g1 = nx.gnp_random_graph(n, k / n)
    g2 = nx.gnp_random_graph(n, k / n)

    # label the nodes
    nx.relabel_nodes(g2, lambda x: x + len(g1.nodes()), copy=False)
    for e in g1.edges():
        g1.edges[e]['num'] = 1
    for e in g2.edges():
        g2.edges[e]['num'] = 2
    for node in g1.nodes():
        g1.nodes[node]['num'] = 1
    for node in g2.nodes():
        g2.nodes[node]['num'] = 2

    # union graph
    G = nx.union(g1, g2)
    n1 = set(g1.nodes())
    n2 = set(g2.nodes())

    # make a fully connected graph
    while n1:
        a = n1.pop()
        while n2:
            b = n2.pop()
            break
        G.add_edge(a, b, Value=3)
    return G, g1, g2
