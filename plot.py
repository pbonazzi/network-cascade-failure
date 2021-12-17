from src.attack import *
from src.create import *
from src.measure import *

## focus on 2 to 3
#ER250= np.loadtxt('./notebooks/results/sy/er/scale/ERn250s.csv',delimiter=",")
#ER500= np.loadtxt('./notebooks/results/sy/er/scale/ERn500s.csv',delimiter=",")

#plot_pinf([ER250, ER500], k=4, labels= ["ER model, N=250, <k>=4","ER model, N=500"], path="./notebooks/figure/ER_250_500.png", p_theory=True)


## normal plot 
#ER250= np.loadtxt('./notebooks/results/sy/er/t20/ERn250k4.csv',delimiter=",")
ER500= np.loadtxt('./notebooks/results/sy/er/t20/ERn500k4.csv',delimiter=",")
ER1000= np.loadtxt('./notebooks/results/sy/er/t20/ERn1000k4.csv',delimiter=",")
ER2000= np.loadtxt('./notebooks/results/sy/er/t20/ERn2000k4.csv',delimiter=",")

plot_pinf([ER500, ER1000, ER2000], k=4,labels= ["ER model, N=500, <k>=4","ER model, N=1000", "ER model, N=2000"], path="./notebooks/figure/ER_t20.png", p_theory=True)



### plot p_inf of interdependent network

#pinf_int_mt = generate_pinf_real(n_file, e_file, edges_m_tr, t=50)
#np.savetxt('./notebooks/results/Paris_train_metro_new_t50.csv', pinf_int_mt, delimiter=',')

#p_inf_t = np.loadtxt('./notebooks/results/single_train_t50.csv', delimiter=",")
#p_inf_m = np.loadtxt('./notebooks/results/single_metro_t50.csv', delimiter=",")
#p_inf_int = np.loadtxt('./notebooks/results/PARIS/Paris_train_metro_new_t50.csv', delimiter=",")
#residual = pinf_int_mt[1][0]

#plot_pinf([[p_inf_int[0], p_inf_int[1]]], labels=['Real world interdependent Network'], path="./notebooks/figure/PARIS/real_world.png", residual = True)

#plot_pinf([[pinf_int_mt[0], pinf_int_mt[1]]], path='./notebooks/figure/realWorld/real_int_net_scaled_t50.png', residual = True)
'''
'''