import numpy as np
import networkx as nx
from matplotlib import pyplot as plt
from datetime import datetime
from time import sleep
from tqdm import tqdm
import src.create as gen_rand
import src.attack as att


def generate_pinf_ER(n, k, t=5, hasGraph=False, files=[]):
    """
    generate p_inf of ER model along with the 1-p from [0,1]

    parameters
    - n : [int] a number of nodes in the network
    - k : [int] an average degree in the network
    - t     : [int] a number of iteration to calculate the mean result

    return 
    - [list] tuple of p and p_inf
        - ps     : [1d array] a probability of being attacked for each node
        - p_infs : [1d array] a probability of mutually connected giant component

    """
    if hasGraph:
        g1 = nx.read_gpickle(files[0])
        g2 = nx.read_gpickle(files[1])
        G_int = nx.read_gpickle(files[2])
        print("...Interdependent Graph Data were given!")
    else:
        start = datetime.now()
        g1 = gen_rand.networkER_w_3Dpos(n, k, 1)
        g2 = gen_rand.networkER_w_3Dpos(n, k, 2)
        G_int = gen_rand.intd_random_net(g1, g2)
        time = datetime.now() - start
        print("...Interdependent Graph Generate Done!", time)
    # g1 = nx.gnp_random_graph(n, k/n)
    # g2 = nx.gnp_random_graph(n, k/n)

    p_infs = []

    ps = np.linspace(0.3, 1.0, 10)

    for p in tqdm(ps):
        print("P(success) = ", p)
        mean_p_inf = 0
        start = datetime.now()
        for i in range(t):
            print("Test time num", i, "/", t)
            # attack G with different p and compute p_inf
            G_att = att.attack_network(G_int, g1, g2, p, False)
            p_inf = compute_pinf(G_att, G_int)
            mean_p_inf += p_inf[0]
        p_infs.append(mean_p_inf / t)
    time = datetime.now() - start
    print("...test: '%f' is Done!" % (p), time)
    return ps, np.array(p_infs)


def generate_pinf_SF(n=50, gamma=3, t=5, hasGraph=False, files=[]):
    """
    generate p_inf of Scale-free model along with the 1-p from [0,1]

    parameters
    - n     : [int] a number of nodes in the network
    - gamma : [int] an expected gamma value of the power law degree distribution
    - t     : [int] a number of iteration to calculate the mean result
    - hasGraph : [Bool] Check whether using given SF graph data or creating new SF graph
    - files : [path list] When hasGraph is True, It is used for the file paths [g1,g2,G]

    return
    - [list] tuple of p and p_inf
        - ps     : [1d array] a probability of being attacked for each node
        - p_infs : [1d array] a probability of mutually connected giant component


    """
    if hasGraph:
        g1 = nx.read_gpickle(files[0])
        g2 = nx.read_gpickle(files[1])
        G_int = nx.read_gpickle(files[2])
        print("...Interdependent Graph Data were given!")
    else:
        start = datetime.now()
        g1 = gen_rand.networkSF_w_3Dpos_PowerL(n, gamma, 1)
        g2 = gen_rand.networkSF_w_3Dpos_PowerL(n, gamma, 2)
        G_int = gen_rand.intd_random_net(g1, g2)
        time = datetime.now() - start
        print("...Interdependent Graph Generate Done!", time)

    p_infs = []
    ps = np.linspace(0.3, 0.9, 20)

    for p in ps:
        mean_p_inf = 0
        start = datetime.now()
        for i in range(t):
            # attack G with different p and compute p_inf
            G_att = att.attack_network(G_int, g1, g2, p, False)
            p_inf = compute_pinf(G_att, G_int)
            mean_p_inf += p_inf[0]
        p_infs.append(mean_p_inf / t)
        time = datetime.now() - start
        print("...test: '%f' is Done!" % (p), time)

    return ps, np.array(p_infs)


def generate_pinf_real(n_file, e_file, edges_crosslayer, order=['metro', 'train'], t=50):
    start = datetime.now()

    g1, df_n_metro, df_e_metro = gen_rand.paris_GenTranspNet(n_file, e_file, order[0], 1)
    g2, df_n_train, df_e_train = gen_rand.paris_GenTranspNet(n_file, e_file, order[1], 2)

    G_int, e_m_tr = gen_rand.paris_GenMultiTranspNet(g1, g2, edges_crosslayer)

    time = datetime.now() - start
    print("...Interdependent Graph Generate Done!", time)

    p_infs = []
    p_infs_layer1 = []
    p_infs_layer2 = []

    ps = np.linspace(0, 1, 20)

    for p in ps:
        mean_p_inf = 0
        mean_p_inf_layer1 = 0
        mean_p_inf_layer2 = 0

        start = datetime.now()
        for i in range(t):
            # attack G with different p and compute p_inf
            G_att = att.attack_network(G_int, g1, g2, p, False)
            G_casc, gcas1, gcas2 = att.cascade_rec(G_int, g1, g2, 1, False)
            comp_set = list(nx.connected_components(G_casc))
            giant_comp = max(comp_set, key=len)

            p_inf, p_inf_layer1, p_inf_layer2 = compute_pinf(G_att, G_int, mut=len(giant_comp))

            mean_p_inf += p_inf
            mean_p_inf_layer1 += p_inf_layer1
            mean_p_inf_layer2 += p_inf_layer2

        p_infs.append(mean_p_inf / t)
        p_infs_layer1.append(mean_p_inf_layer1 / t)
        p_infs_layer2.append(mean_p_inf_layer2 / t)

        time = datetime.now() - start
        print("...test: '%f' is Done!" % (p), time)

    return ps, np.array(p_infs), np.array(p_infs_layer1), np.array(p_infs_layer2)


def generate_pinf_real_single(G_single, t=50):
    p_infs = []
    ps = np.linspace(0, 1, 20)

    for p in ps:
        mean_p_inf = 0
        for i in range(t):
            # attack G with different p and compute p_inf
            G_att = att.attack_network(G_single, p=p)
            print("p :", p)
            p_inf = compute_pinf(G_att, G_single)
            mean_p_inf += p_inf
        p_infs.append(mean_p_inf / t)

    return ps, np.array(p_infs)


def compute_pinf(G_att, G_init, mut=None):
    """
    compute a probability of mutually connected giant component which is
    the probability that a node belongs to the largest connected component

    parameters
     - G_att : [Graph] networkx graph after attacked

    return
     - p_inf : [float] number of nodes belong to the giant component / total number of nodes

    """

    if len(G_att.nodes()) == 0:
        print("[W] : Computing probabilities for an empty graph returns 0.")
        return 0
    total_num_nodes = len(list(G_init))

    if mut != None:
        total_num_nodes = mut  # cacasde recursive first and then measure the connected components.

    comp_set = list(nx.connected_components(G_att))
    giant_comp = max(comp_set, key=len)
    layer1, layer2 = giant_layercount(G_att, giant_comp)  # count layer1 and layer2 in Giant Component after cascading.
    print("giant comp_set layer count: ", layer1, layer2, len(giant_comp))

    comp_set_init = list(nx.connected_components(G_init))
    giant_comp_init = max(comp_set_init, key=len)
    layer1_init, layer2_init = giant_layercount(G_init,
                                                giant_comp_init)  # count layer1 and layer2 initial Giant Component

    p_inf = len(giant_comp) / len(giant_comp_init)
    p_inf_layer1 = layer1 / layer1_init
    p_inf_layer2 = layer2 / layer2_init
    # p_inf = len(giant_comp) / total_num_nodes

    return p_inf, p_inf_layer1, p_inf_layer2


def plot_pinf(results, k=1, xlim=None, labels=None, path=None, p_theory=False, residual=False):
    """
    plotting the figure of p*k vs p_inf

    parameters
    - results : [list] tuple of p and p_inf
    - k       : [int]  average degree of the network
    - labels  : [list] label for each result (number of nodes)
    - path    : [string] path to save the figure
    - p_theory: [float] theoretical value of p_c

    """
    plt.figure(figsize=(10, 7))
    plt.rcParams.update({'font.size': 14})
    color = iter(plt.cm.rainbow(np.linspace(0.0, 1, len(results))))
    marker = ['o', 's', 'D', 'v']

    for i, res in enumerate(results):
        pks = res[0] * k
        p_infs = res[1]

        plt.plot(pks, p_infs, c=next(color), linewidth=2, marker=marker[i], mfc="None")

    if p_theory:
        plt.vlines(2.4554, ymin=0, ymax=1, colors='k', linestyles='dashdot', label='$p_{c}$=2.4554/<k>')
    if k > 1:
        plt.xlabel('p<k>')
    else:
        plt.xlabel('p')
        # plt.xlabel('$P_{node}$(fail)')
    if residual:
        plt.hlines(results[0][1][0], xmin=0, xmax=1, linestyles='dotted', colors='k')
    plt.ylabel('$P_{inf}$')
    # plt.xlim(0,0.9)
    plt.ylim(0, 1)
    # plt.ylabel('$P_{node}$(in Gcomponent)')
    if labels:
        plt.legend(labels)
    plt.savefig(path, dpi=300, bbox_inches='tight')
    plt.grid()
    plt.show()


def giant_layercount(G, giant_comp):
    layer1 = 0
    layer2 = 0
    layer_dict = dict(nx.get_node_attributes(G, "layer"))
    for node in giant_comp:
        layer = layer_dict[node]
        if layer == 1:
            layer1 += 1
        else:
            layer2 += 1
    return layer1, layer2
