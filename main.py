from src.attack import *
from src.create import *
from src.measure import *

### Analysis Real data - Paris train & metro Network
e_file = "./data/edge/edge.csv"
n_file = "./data/vertex/vertex.csv"
edges_m_tr = "./data/edge/edge_m_tr.csv"

   
G_train, df_n_train, df_e_train = paris_GenTranspNet(n_file,e_file,'train',1)
G_metro, df_n_metro, df_e_metro = paris_GenTranspNet(n_file,e_file,'metro',2)

G_int_mt, e_m_tr = paris_GenMultiTranspNet(G_metro, G_train, edges_m_tr)

## calculating <k> of real dataset

k_train = 2*G_train.number_of_edges() / G_train.number_of_nodes()
k_metro = 2*G_metro.number_of_edges() / G_metro.number_of_nodes()
k_int_mt = 2*G_int_mt.number_of_edges() / G_int_mt.number_of_nodes()

print("<k> of train network: ", k_train)
print("<k> of metro network: ", k_metro)
print("<k> of interdependent network: ", k_int_mt)

'''
### plot p_inf of single network
p_inf_m = generate_pinf_real_single(G_metro, t=10)
p_inf_t = generate_pinf_real_single(G_train, t=10)


np.savetxt('./notebooks/results/single_train_new.csv', p_inf_t, delimiter=',')
np.savetxt('./notebooks/results/single_metro_new.csv', p_inf_m, delimiter=',')

#p_inf_t = np.loadtxt('./notebooks/results/single_train.csv', delimiter=",")
#p_inf_m = np.loadtxt('./notebooks/results/single_metro.csv', delimiter=",")

plot_pinf([p_inf_t, p_inf_m], labels=['Paris Train Network', 'Paris Metro Network'], path="./notebooks/figure/test.png")

'''

### plot p_inf of interdependent network

#pinf_int_mt = generate_pinf_real(n_file, e_file, edges_m_tr, t=10)
#np.savetxt('./notebooks/results/Paris_train_metro_new.csv', pinf_int_mt, delimiter=',')

pinf_int_mt = np.loadtxt('./notebooks/results/Paris_train_metro_new.csv', delimiter=",")
residual = pinf_int_mt[1][0]

plot_pinf([[pinf_int_mt[0], pinf_int_mt[1]-residual]], labels=["train-metro"], path='./notebooks/figure/real_int_net_scaled.png')