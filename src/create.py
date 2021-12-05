import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import powerlaw
import pandas as pd


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
        g1.edges[e]['layer'] = 1
    for e in g2.edges():
        g2.edges[e]['layer'] = 2
    for node in g1.nodes():
        g1.nodes[node]['layer'] = 1
    for node in g2.nodes():
        g2.nodes[node]['layer'] = 2

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


def nodeSetting(G, layer=1):
    """ Generate (x,y,z) coordinates, Node ID and Attribute Setting for cascade methods

    (x,y) coordinates follow the networkx spring layout.
    z coordinates(Layer) is given as a parameter 'layer'
    Save (x,y,z) coordinates as an attribute of node named '3D_pos'
    This information is used for drawing interdependent graph

    Parameters
    ----------
    G : Network Graph
    layer : Layer of this graph
    
    """
    # Node Attribute '3D_pos' added
    pos = nx.spring_layout(G)
    for node in pos.keys():
        pos[node] = np.append(pos[node], layer)
    nx.set_node_attributes(G, pos, name='3D_pos')

    # Node Attribute 'layer' added
    for e in G.edges():
        G.edges[e]['layer'] = layer
    for node in G.nodes():
        G.nodes[node]['layer'] = layer

    # Node Renaming
    mapping = {}
    for node in G.nodes():
        mapping[node] = str(layer) + '-' + str(node)

    H = nx.relabel_nodes(G, mapping)

    return H

def Paris_NodeSetting (G,df_vertex,Layer_num=1):

    attrs = {}
    _ = {}
    for data in df_vertex.values:
        _ = {}
        _['Lat'] = data[1]
        _['Lon'] = data[2]
        _['Layer'] = Layer_num
        _['3D_pos'] = np.array([_['Lat'],_['Lon'],Layer_num])
        attrs[data[0]] = _
    nx.set_node_attributes(G,attrs)

    return G


def SF_powerlaw_exp(G):
    """ Calculate gamma value of power-law degree distribution

    Parameters
    ----------
    G : Network Graph

    Returns
    -------
    alpha : gamma value of power-law degree distribution
    
    """

    d = [G.degree()[i] for i in G.nodes()]

    fit = powerlaw.Fit(d, discrete=True, verbose=False)
    alpha = fit.power_law.alpha

    return alpha


def networkER_w_3Dpos(N, avgdegree, layer=1):
    """ Create Erdos-Renyi Network with 3D position attribute

    Parameters
    ----------
    N : Number of nodes
    avgdegree : Expected average degree
    layer : Layer of this graph (refer to the method 'nodeSetting')

    Returns
    -------
    H : ER Networkx Graph

    """

    G = nx.erdos_renyi_graph(N, avgdegree / N)
    H = nodeSetting(G, layer)

    return H

def networkSF_w_3Dpos_BA(N, m, layer=1):
    """ Create Scale-Free Network following Barabasi Albert Model with 3D position attribute

    Parameters
    ----------
    N : Number of nodes
    m : Number of edges to attach from a new node to existing nodes
    layer : Layer of this graph (refer to the method 'nodeSetting')

    Returns
    -------
    H : Scale Free Barabasi Albert Networkx Graph

    """
    G = nx.barabasi_albert_graph(N, m)
    H = nodeSetting(G, layer)

    return H

def networkSF_w_3Dpos_PowerL(N, gamma, layer=1):
    """ Create Scale-Free Network following PowerLaw Degree Distribution with 3D position attribute

    Parameters
    ----------
    N : Number of nodes
    gamma : Expected gamma value of powerlaw degree distribution 
    layer : Layer of this graph (refer to the method 'add_3Dpos_attributes')

    Returns
    -------
    H : Scale Free Powerlaw Degree Distribution Networkx Graph

    """

    T = 1000
    i = 0
    # print("degree sequence Erdos Gallai 1")
    while i < T:
        s = []

        s = powerlaw.Power_Law(xmin=2, parameters=[gamma]).generate_random(N).astype('int')
        
        # Returns True if deg_sequence can be realized by a simple graph.
        # The validation is done using the Erdős-Gallai theorem
        if nx.is_valid_degree_sequence_erdos_gallai(s):

            G = nx.configuration_model(s)
            G = nx.Graph(G)  # remove parallel edges
            G.remove_edges_from(nx.selfloop_edges(G))  # remove selfloop edges

            gamma_real = SF_powerlaw_exp(G)
            r_gamma_real = round(gamma_real, 1)  # check the powerlaw gamma value (rounded at decimal place 1)

            if (r_gamma_real == gamma):
                break
        i += 1


    if (i == 1000):
        print("Couldn't generate Scale-Free Network based on given powerLaw parameters. Last gamma:", gamma_real)
    else:
        print("Generate Scale-Free Network based on given powerLaw parameters\n(iter: %d. Last gamma:%f)" %(i,gamma_real))

    H = nodeSetting(G, layer)

    return H

def ParisTranspNetwork (vertex_csv, edge_csv, LayerName):
    df_vertex = pd.read_csv(vertex_csv)
    df_edge = pd.read_csv(edge_csv)

    transp_vertex = df_vertex['Layer']==LayerName
    transp_edge = df_edge['Layer']==LayerName

    df_vertex_transp = df_vertex[transp_vertex]
    df_edge_transp = df_edge[transp_edge]

    G = nx.from_pandas_edgelist(df_edge_transp, '# Source NodeID','Target NodeID',['Layer','name'])
    
    return G, df_vertex_transp, df_edge_transp


def intd_random_net(G_a, G_b):
    """ Create an interdependent network from two Random Network

    Link two Random Network based on each Node ID
    Each ER Network should have same node size

    Parameters
    ----------
    G_a : First Network Graph
    G_a : Second Network Graph

    Returns
    -------
    intd_G : Networkx Graph

    """
    _ = list(G_a.nodes())[0]
    a_layer = _.split('-')[0]
    _ = list(G_b.nodes())[0]
    b_layer = _.split('-')[0]

    intd_G = nx.union(G_a, G_b)

    if len(G_a.nodes()) == len(G_b.nodes()):

        n1 = set(G_a.nodes())
        n2 = set(G_b.nodes())

        for i in range(len(G_a.nodes())):
            intd_G.add_edge(a_layer + '-' + str(i),
                            b_layer + '-' + str(i))  # Link between two nodes which has same node id.

    else:
        print("ERROR : Given two networks has different network size")

    return intd_G

def intdNetworkDraw(intd_G):
    """ Draw Interdependent Network

    Refer to each node's 3D coordinates.

    Parameters
    ----------
    intd_G : Interdependent Network Graph from the method 'intd_RAND_networks'

    """
    fig = plt.figure(figsize=(10, 10))
    ax = plt.axes(projection='3d')
    color = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

    n_attr = nx.get_node_attributes(intd_G, '3D_pos')

    for node in n_attr.keys():
        pos = n_attr[node]
        x, y, z = [i for i in pos]
        ax.scatter(x, y, z, c=color[int(z)])

    for edge in list(intd_G.edges):

        pos_a, pos_b = [n_attr[i] for i in edge]
        x_a, y_a, z_a = [i for i in pos_a]
        x_b, y_b, z_b = [i for i in pos_b]

        if z_a != z_b:
            alpha = 0.5  # If the edge connect two nodes in different layer, the edge transparency set differently.
        else:
            alpha = 1
        ax.plot([x_a, x_b], [y_a, y_b], [z_a, z_b], color="tab:gray", alpha=alpha)

    ax.set_axis_off()
    plt.show()
    return