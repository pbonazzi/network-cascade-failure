import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import powerlaw

def add_3Dpos_attributes (G,z_pos=1):
    """ Generate (x,y,z) coordinates for each node

    (x,y) coordinates follow the networkx spring layout.
    z coordinates(Layer) is given as a parameter 'z_pos'
    Save (x,y,z) coordinates as an attribute of node named '3D_pos'
    This information is used for drawing interdependent graph

    Parameters
    ----------
    G : Network Graph
    z_pos : Layer of this graph
    
    """    
    pos = nx.spring_layout(G)
    for node in pos.keys():
        pos[node] = np.append(pos[node],z_pos)
    nx.set_node_attributes(G,pos,name='3D_pos')

    return

def SF_powerlaw_exp (G):
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


def networkER_w_3Dpos(N, avgdegree, z_pos=1):
    """ Create Erdos-Renyi Network with 3D position attribute

    Parameters
    ----------
    N : Number of nodes
    avgdegree : Expected average degree
    z_pos : Layer of this graph (refer to the method 'add_3Dpos_attributes')

    Returns
    -------
    ER : Networkx Graph

    """    

    ER = nx.erdos_renyi_graph(N, avgdegree/N)
    add_3Dpos_attributes(ER,z_pos)

    for e in ER.edges():
        ER.edges[e]['num'] = z_pos
    for node in ER.nodes():
        ER.nodes[node]['num'] = z_pos

    return ER

def networkSF_w_3Dpos_BA(N,m,z_pos=1):
    """ Create Scale-Free Network following Barabasi Albert Model with 3D position attribute

    Parameters
    ----------
    N : Number of nodes
    m : Number of edges to attach from a new node to existing nodes
    z_pos : Layer of this graph (refer to the method 'add_3Dpos_attributes')

    Returns
    -------
    SF_BA : Networkx Graph

    """    
    SF_BA = nx.barabasi_albert_graph(N,m)
    add_3Dpos_attributes(SF_BA,z_pos)

    for e in SF_BA.edges():
        SF_BA.edges[e]['num'] = z_pos
    for node in SF_BA.nodes():
        SF_BA.nodes[node]['num'] = z_pos

    return SF_BA

def networkSF_w_3Dpos_PowerL(N,gamma,z_pos=1):
    """ Create Scale-Free Network following PowerLaw Degree Distribution with 3D position attribute

    Parameters
    ----------
    N : Number of nodes
    gamma : Expected gamma value of powerlaw degree distribution 
    z_pos : Layer of this graph (refer to the method 'add_3Dpos_attributes')

    Returns
    -------
    SF_PowerL : Networkx Graph

    """ 

    T = 1000
    i = 0
    while i<T: 
        s=[]

        while len(s)<N: # N nodes, power-law gamma without zero degree
            nextval = int(nx.utils.powerlaw_sequence(1, gamma)[0])
            if nextval!=0:
                s.append(nextval)
                
        if (sum(s)%2 == 0): #  As each edge contains two vertices, the degree seq sum has to be even.

            SF_PowerL = nx.configuration_model(s)
            SF_PowerL = nx.Graph(SF_PowerL) # remove parallel edges
            SF_PowerL.remove_edges_from(nx.selfloop_edges(SF_PowerL)) # remove selfloop edges

            gamma_real = SF_powerlaw_exp(SF_PowerL)
            r_gamma_real = round(gamma_real,1) # check the powerlaw gamma value (rounded at decimal place 1)

            if (r_gamma_real==gamma):
                break

        i += 1
    
    add_3Dpos_attributes(SF_PowerL,z_pos)

    for e in SF_PowerL.edges():
        SF_PowerL.edges[e]['num'] = z_pos
    for node in SF_PowerL.nodes():
        SF_PowerL.nodes[node]['num'] = z_pos

    if (i == 1000):
        print("Couldn't generate Scale-Free Network based on given powerLaw parameters. Last gamma:", gamma_real)
    else:
        print("Generate Scale-Free Network based on given powerLaw parameters. Last gamma:", gamma_real)

    return SF_PowerL


def intd_random_net (G_a,G_b):
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

    intd_G = nx.union(G_a,G_b, rename=('a-','b-'))

    if len(G_a.nodes()) == len(G_b.nodes()):
        for i in range(len(G_a.nodes())):
            intd_G.add_edge('a-'+str(i),'b-'+str(i)) # Link between two nodes which has same node id.
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
    fig = plt.figure(figsize=(10,10))
    ax = plt.axes(projection='3d')

    n_attr = nx.get_node_attributes(intd_G,'3D_pos')
    for node in n_attr.keys():
        pos = n_attr[node]
        x,y,z = [ i for i in pos]
        if node.startswith('a-'):
            color = 'b'
        elif node.startswith('b-'):
            color = 'g'
        else:
            color = 'r'
        ax.scatter(x,y,z,c=color)

    for edge in list(intd_G.edges):
        pos_a, pos_b = [n_attr[i] for i in edge]
        x_a,y_a,z_a = [i for i in pos_a]
        x_b,y_b,z_b = [i for i in pos_b]

        if z_a != z_b:
            alpha = 0.5 # If the edge connect two nodes in different layer, the edge transparency set differently.
        else:
            alpha = 1
        ax.plot([x_a,x_b],[y_a,y_b],[z_a,z_b],color="tab:gray",alpha=alpha)

    
    ax.set_axis_off()
    plt.show()
    return
