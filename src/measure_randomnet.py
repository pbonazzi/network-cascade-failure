import numpy as np
import networkx as nx
from matplotlib import pyplot as plt

import gen_randomnet as gen_rand
import cascadeflr as cascade 


def compute_pinf(G_att):
    '''
    compute a probability of mutually connected giant component which is 
    the probability that a node belongs to the largest connected component 

    p_inf = number of nodes belong to the giant component / total number of nodes

    parameters  
     - G_att : networkx graph after attacked

    return
     - p_inf : 

    '''
    total_num_nodes = len(list(G_att))
    comp_set = list(nx.connected_components(G_att))
    print(comp_set)
    giant_comp = max(comp_set, key=len)
    
    p_inf = len(giant_comp)/total_num_nodes

    return p_inf


def generate_pinf_ER(n, k):
    '''
    generate p_inf of ER model along with the 1-p from [0,1]

    parameters 
    - n : [int] a number of nodes in the network
    - k : [int] an average degree in the network

    return
    - ps     : [list] a probabilty of being attacked for each node
    - p_infs : [list] a probability of mutually connected giant component
    
    '''
    
    #g1 = nx.gnp_random_graph(n, k/n)
    #g2 = nx.gnp_random_graph(n, k/n)
    g1 = gen_rand.networkER_w_3Dpos(n, k, 1)
    g2 = gen_rand.networkER_w_3Dpos(n, k, 2)
    G_int = gen_rand.intd_random_net(g1, g2)
    
    p_infs = []
    ps = np.linspace(0.1,0.9,10) 
    
    for p in ps:
        mean_p_inf = 0
        t=5
        for i in range(t):
            # attack G with different p and compute p_inf
            G_att = cascade.attack_network(G_int, g1, g2, p)
            print(len(list((G_att))))
            p_inf = compute_pinf(G_att)
            mean_p_inf += p_inf/t
        p_infs.append(mean_p_inf)
    
    return ps, p_infs   


def generate_pinf_SF(n, gamma):
    '''
    generate p_inf of Scale-free model along with the 1-p from [0,1]

    parameters 
    - n     : [int] a number of nodes in the network
    - gamma : [int] an expected gamma value of the powerlaw degree distribution 

    return
    - ps     : [list] a probabilty of being attacked for each node
    - p_infs : [list] a probability of mutually connected giant component
    
    '''
    
    g1 = gen_rand.networkSF_w_3Dpos_PowerL(n, gamma, 1)
    g2 = gen_rand.networkSF_w_3Dpos_PowerL(n, gamma, 2)
    G_int = gen_rand.intd_random_net(g1, g2)
    
    p_infs = []
    ps = np.linspace(0.1,0.9,10) 
    
    for p in ps:
        mean_p_inf = 0
        t=5
        for i in range(t):
            # attack G with different p and compute p_inf
            G_att = cascade.attack_network(G_int, g1, g2, p)
            p_inf = compute_pinf(G_att)
            mean_p_inf += p_inf/t
        p_infs.append(mean_p_inf)
    
    return (ps, p_infs)   


def plot_pinf(results, k, labels, path=None, p_theory = False):
    '''
    plotting the figrue of p*k vs p_inf 

    parameters 
    - results : [list] tuple of p and p_inf
    - k       : [int]  average degree of the network
    - labels  : [list] label for each result (number of nodes)
    - path    : [string] path to save the figure
    - p_theory: [float] theoritical value of p_c 

    '''

    for i, res in enumerate(results):

        pks = res[0]*k
        p_infs = res[1]
        
        plt.plot(pks, p_infs, 'o-', label = labels[i])


    plt.xlabel('p')
    plt.ylabel('p_inf')
    plt.legend()
    plt.savefig(path, dpi=300, bbox_inches='tight')
    plt.show()
    
    