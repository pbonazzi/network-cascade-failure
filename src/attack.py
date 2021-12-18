# %%
import networkx as nx
import numpy as np


def foreign_neighbors(node, G):
    """ Find the set of all neighbor nodes that initially came from a different network


    Parameters
    ----------
    node node : a node from the graph
    Graph G : any networkx graph

    Return
    ----------
    set : set of foreign neighbors

    """

    foreign = []
    numb = G.nodes[node]['layer']
    s = set(G.neighbors(node))
    while s:
        x = s.pop()
        if G.nodes[x]['layer'] != numb:
            foreign.append(x)
    if len(foreign) == 0:
        foreign = []

    return set(foreign)


# %%
def cascade_fail(G, g1, g2, target, verbose=False):
    """Original graphs without the target node and all neighboring nodes that originally came from the other network.


    Parameters
    ----------
    Graph G, g1, g2
    node target : target node
    bool verbose : visualize results

    Return
    ----------
    Graph G2 , g1 , g2 : updated graphs

    """
    G2 = G.copy()

    # if interconnected network
    # remove neighboring nodes from the other network
    interconnected = (len(g1.nodes()) != 0 and len(g2.nodes()) != 0)
    if interconnected:
        num = G.nodes[target]['layer']
        foreign_nodes = foreign_neighbors(target, G)
        if foreign_nodes != set([]):
            for neigh in foreign_nodes:
                G2.remove_node(neigh)
                if num == 2:
                    g1.remove_node(neigh)
                else:
                    g2.remove_node(neigh)
                if verbose:
                    print('Deleted neighbour', neigh)

    # remove target node
    G2.remove_node(target)
    if interconnected:
        if num == 1:
            g1.remove_node(target)
        else:
            g2.remove_node(target)

    return G2, g1, g2


def cascade_rec(G, g1, g2, counter, verbose):
    """Remove the edges of distant nodes .

    Process
    ----------
       Get the edges in g2. For each node of the edge pair, find their foreign neighbors.
       If nodes in these two sets are in different clusters in g1, remove the edge pair connection in g2 and G.

    Parameters
    ----------
     Graph G , g1, g2 : networkx graphs
     int counter :
     bool verbose : visualize results

    Return
    ----------
    Graph G2 : networkx graphs

    """

    removed = 0

    # get the edges in g2
    edges = set(g2.edges())

    # get list of connected components for g1
    components = list(nx.connected_components(g1))

    # For each edge pair (a,b) find the foreign neighbors of node a and b.
    # If these neighbors are in different clusters delete the edge (a,b).
    while edges:
        a, b = edges.pop()
        n1 = foreign_neighbors(a, G)
        n2 = foreign_neighbors(b, G)
        if n1 == set([]) or n2 == set([]):
            continue
        for comp in components:
            if (n1.issubset(comp) and not n2.issubset(comp)) or (not n1.issubset(comp) and n2.issubset(comp)):
                G.remove_edge(a, b)
                g2.remove_edge(a, b)

                removed = 1
                if verbose:
                    print('Removed', tuple((a, b)))
                    break

    # if we removed an edge, change perspective and look for others.
    if removed == 1:
        cascade_rec(G, g2, g1, 1, verbose)

    # if un successful, change perspective once again, but decrease counter by one to eventually stop recursion.
    if removed == 0 and counter > 0:
        cascade_rec(G, g2, g1, counter - 1, verbose)

    return G, g1, g2


# %%
def cascade_rec_optional(G, g1, g2, counter, verbose):
    """Invented method to remove edges in Stage 2,3.

    Process
    ----------
       Get the edges in g2. For each node of the edge pair, find their foreign neighbors.
       If at least one node for each of these two sets are in the same clusters in g1, maintain the pair connection in g2 and G.

    Parameters
    ----------
     Graph G , g1, g2 : networkx graphs
     int counter : 
     bool verbose : visualize results

    Return
    ----------
    Graph G2 : networkx graphs

    """

    removed = 0

    # get the edges in g2
    edges = set(g2.edges())

    # get list of connected components for g1
    components = list(nx.connected_components(g1))

    # For each edge pair (a,b) find the foreign neighbors of node a and b.
    # If these neighbors are in different clusters delete the edge (a,b).
    while edges:
        a, b = edges.pop()
        n1 = foreign_neighbors(a, G)
        n2 = foreign_neighbors(b, G)
        if n1 == set([]) or n2 == set([]):
            continue
        mutually = 0
        for i, comp in enumerate(components):
            """
            set mutually connected components 
            set of neighbour nodes n1
            set of neighbour nodes n2
            """
            for neigh1 in n1:
                for neigh2 in n2:
                    if {neigh1}.issubset(comp) and {neigh2}.issubset(comp):
                        mutually = 1
                    if mutually == 1:
                        break
                if mutually == 1:
                    break
            if mutually == 1:
                break
        if mutually == 0:
            G.remove_edge(a, b)
            g2.remove_edge(a, b)

            removed = 1
            if verbose:
                print('Removed', tuple((a, b)))

    # if we removed an edge, change perspective and look for others.
    if removed == 1:
        cascade_rec(G, g2, g1, 1, verbose)

    # if un successful, change perspective once again, but decrease counter by one to eventually stop recursion.
    if removed == 0 and counter > 0:
        cascade_rec(G, g2, g1, counter - 1, verbose)

    return G, g1, g2


# %%
def attack_network(G, g1=nx.Graph(), g2=nx.Graph(), p=0.5, verbose=True):
    """ Entry function called in the main. Select the nodes to be attacked and run the cascade failure on each target.

    Parameters
    ----------
    Graph G, g1, g2 : networkx graphs
    bool union : specifies if there are two graph combined 
    float p : probability that each node is deleted
    bool verbose : visualize results

    Return
    ----------
    Graph G : a networkx graph

    """
    # we keep and update the  sub-networks to detect the connected components
    g1 = g1.copy()
    g2 = g2.copy()
    G = G.copy()

    # randomly select node to remove from network g1 (or A in paper)
    candidates = set()
    nodes = g1.nodes()
    single = (len(nodes) == 0)
    if single:
        nodes = G.nodes()

    for node in nodes:
        if np.random.random() < 1 - p:
            candidates.add(node)

    # print(candidates)
    # delete nodes and update the set
    while candidates:
        target = candidates.pop()
        if verbose:
            print('attacking', target)
        G, g1, g2 = cascade_fail(G, g1, g2, target=target, verbose=verbose)
        nodes_updated = set(G.nodes())
        candidates.intersection_update(nodes_updated)

    # recursively detect clusters and remove connecting links from neighboring network by switching g1=g2 and g2=g1
    # G3,g1,g2 = cascade_rec(G2,g1,g2,1,verbose)
    if not single:
        G, g1, g2 = cascade_rec(G, g1, g2, 1, verbose)

    return G
