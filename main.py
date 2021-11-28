import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def load_graph(filepath):
    try:
        return nx.read_gml(filepath)
    except nx.NetworkXError:
        return nx.read_graphml(filepath)


def draw_graph(graph, filename):
    pos = nx.spring_layout(graph)
    plt.figure(3, figsize=(10, 8))
    plt.title(filename)
    nx.draw(graph, with_labels=False, node_size=50, pos=pos)
    plt.show()


def degree_vec(graph):
    return np.asarray([d for d in dict(graph.degree()).values()])


path = "data/gml/multigraph.gml"

paris = load_graph(path)

# draw_graph(paris, "Paris")

print("DEGREE VECTOR : ", degree_vec(paris))