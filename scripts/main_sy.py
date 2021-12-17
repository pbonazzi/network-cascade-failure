from src.attack import *
from src.create import *
from src.measure import *

'''
## Analisy ER and SF Network 
ERn250s = generate_pinf_ER(250, 4, t=10)
np.savetxt('./notebooks/results/sy/er/scale/ERn250s.csv', ERn250s, delimiter=',')
ERn500s = generate_pinf_ER(500, 4, t=10)
np.savetxt('./notebooks/results/sy/er/scale/ERn500s.csv', ERn500s, delimiter=',')
ERn1000s = generate_pinf_ER(1000, 4, t=10)
np.savetxt('./notebooks/results/sy/er/scale/ERn1000s.csv', ERn1000s, delimiter=',')
ERn1500s = generate_pinf_ER(1500, 4, t=10)
np.savetxt('./notebooks/results/sy/er/scale/ERn1500s.csv', ERn1500s, delimiter=',')
ERn2000s = generate_pinf_ER(2000, 4, t=10)
np.savetxt('./notebooks/results/sy/er/scale/ERn2000s.csv', ERn2000s, delimiter=',')

'''
## lin20 btw 2.00-3.50 (t=30)

ERn4000t15 = generate_pinf_ER(4000, 4, t=15)
np.savetxt('./notebooks/results/sy/er/t20/ERn4000t15.csv', ERn4000t15, delimiter=',')

#ERn8000t5 = generate_pinf_ER(8000, 4, t=5)
#np.savetxt('./notebooks/results/sy/er/t20/ERn8000t5.csv', ERn8000t5, delimiter=',')

'''
'''

#ERn4000k4 = generate_pinf_ER(4000, 4,t=20)
#np.savetxt('./notebooks/results/sy/er/ERn4000k4.csv', ERn4000k4, delimiter=',')  

#ERn8000k4 = generate_pinf_ER(8000, 4,t=20)
#np.savetxt('./notebooks/results/sy/er/ERn8000k4.csv', ERn8000k4, delimiter=',') 

#np.savetxt('./notebooks/results/sy/er/ERn1000k4.csv', ERn1000k4, delimiter=',')  
#np.savetxt('./notebooks/results/sy/er/ERn2000k4.csv', ERn2000k4, delimiter=',')  
#np.savetxt('./notebooks/results/sy/er/ERn4000k4.csv', ERn4000k4, delimiter=',')  
#np.savetxt('./notebooks/results/sy/er/ERn8000k4.csv', ERn8000k4, delimiter=',')  

#ER1000= np.loadtxt('./notebooks/results/1012/ERn1000k4.csv',delimiter=",")
#ER2000= np.loadtxt('./notebooks/results/1012/ERn2000k4.csv',delimiter=",")
#ER4000= np.loadtxt('./notebooks/results/1012/ERn4000k4.csv',delimiter=",")

#plot_pinf([ER1000, ER2000, ER4000], k=4,labels= ["ER model, N=1000, <k>=4","ER model, N=2000, <k>=4","ER model, N=4000, <k>=4"], path="./notebooks/figure/ER_new.png", p_theory=True)


#SFn500g25 = networkSF_w_3Dpos_PowerL(500, )

'''

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


## draw degree distribution 
int_degree = G_int_mt.degree()
print(len(G_int_mt.nodes()))
int_degrees = [int_degree[i] for i in G_int_mt.nodes()]
print(int_degrees)


_ = plt.hist(int_degrees, bins = 50, density = False, edgecolor="white")
plt.yscale('log')

plt.title('Degree distribution of Paris interdependent (Train-Metro) Network')
plt.xlabel('Degree (k)')
#plt.xlim(1,10.1)
plt.ylabel('log (Number of nodes with k)')

plt.show()

''' 
'''

### plot p_inf of single network
p_inf_m = generate_pinf_real_single(G_metro)
p_inf_t = generate_pinf_real_single(G_train)


np.savetxt('./notebooks/results/single_train_t50.csv', p_inf_t, delimiter=',')
np.savetxt('./notebooks/results/single_metro_t50.csv', p_inf_m, delimiter=',')

#p_inf_t = np.loadtxt('./notebooks/results/single_train.csv', delimiter=",")
#p_inf_m = np.loadtxt('./notebooks/results/single_metro.csv', delimiter=",")

plot_pinf([p_inf_t, p_inf_m], labels=['Paris Train Network', 'Paris Metro Network'], path="./notebooks/figure/realWorld/pif_single_real_network_t50.png")





### plot p_inf of interdependent network

#pinf_int_mt = generate_pinf_real(n_file, e_file, edges_m_tr, t=50)
#np.savetxt('./notebooks/results/Paris_train_metro_new_t50.csv', pinf_int_mt, delimiter=',')

p_inf_t = np.loadtxt('./notebooks/results/single_train_t50.csv', delimiter=",")
p_inf_m = np.loadtxt('./notebooks/results/single_metro_t50.csv', delimiter=",")
p_inf_int = np.loadtxt('./notebooks/results/Paris_train_metro_new_t50.csv', delimiter=",")
#residual = pinf_int_mt[1][0]

plot_pinf([p_inf_t, p_inf_m, p_inf_int], labels=['Paris Train Network', 'Paris Metro Network', 'Interdependent Network'], path="./notebooks/figure/realWorld/pif_all_together.png")

#plot_pinf([[pinf_int_mt[0], pinf_int_mt[1]]], path='./notebooks/figure/realWorld/real_int_net_scaled_t50.png', residual = True)
'''


