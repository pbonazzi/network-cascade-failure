# %%
import sys
import networkx as nx
from matplotlib import pyplot as plt
import numpy as np
import json

# %%
import generation as rndm
import cascadeflr as cas
import GenNetwork.gen_randomnet as grndm
import Measure_randomnet as measurerndm

'''
plot p<k> vs p_inf 
'''
# compute p_in with different parameters 
ERn250k4 = generate_pinf_ER(250, 4)   # ER model, node=250, k=4
ERn1000k4 = generate_pinf_ER(1000, 4) # ER model, node=1000, k=4
ERn2000k4 = generate_pinf_ER(2000, 4) # ER model, node=2000, k=4

SFn250k4 = generate_pinf_SF(500, 2.3)   # SF model, node=500, gamma=2.3
SFn1000k4 = generate_pinf_SF(500, 2.7) # SF model, node=500, gamma=2.7
SFn2000k4 = generate_pinf_SF(500, 3) # SF model, node=500, gamma=3

# plot the result (save the figure ./fig)

plot_pinf([ERn250k4,ERn1000k4,ERn2000k4], 4, ["ER, n=250, k=4","ER, n=1000, k=4","ER, n=2000, k=4", path="figure/ER_pinf.png", p_theory = False)
plot_pinf([SFn500g23,SFn500g27,SFn500g3], 4, ["SF, n=500, l=2.3","SF, n=500, l=2.7", "SF, n=500, l=3", path="figure/SF_pinf.png", p_theory = False)



'''
test generating single network and interdependent network
'''
# %%
N, n1, n2 = rndm.new_network(5, 3)
A = cas.attack_network(N, n1, n2, 0.8)

print(":)")

# %%
# 1 ER
ER_a = grndm.networkER_w_3Dpos(20,10,1)
ER_b = grndm.networkER_w_3Dpos(20,10,2)
intd_ER = grndm.intd_random_net(ER_a,ER_b)

print(len(intd_ER.nodes()))
grndm.intdNetworkDraw(intd_ER)
# %%
# 1-1 ER Attacked
intd_ER_attck = cas.attack_network(intd_ER, ER_a, ER_b, 0.8)

print(len(intd_ER_attck.nodes()))
grndm.intdNetworkDraw(intd_ER_attck)
print(":)")

# %%
# 2 SF_BA
SF_BA_a = grndm.networkSF_w_3Dpos_BA(20,2,1)
SF_BA_b = grndm.networkSF_w_3Dpos_BA(20,2,2)
intd_SF_BA = grndm.intd_random_net(SF_BA_a,SF_BA_b)

print(len(intd_SF_BA.nodes()))
grndm.intdNetworkDraw(intd_SF_BA)
# %%
# 2-1 SF_BA Attacked
intd_SF_BA_attck = cas.attack_network(intd_SF_BA, SF_BA_a, SF_BA_b, 0.8)

print(len(intd_SF_BA_attck.nodes()))
grndm.intdNetworkDraw(intd_SF_BA_attck)
print(":)")
# %%
# 3 SF_PowerL
SF_PowerL_a = grndm.networkSF_w_3Dpos_PowerL(100,2.5,1)
SF_PowerL_b = grndm.networkSF_w_3Dpos_PowerL(100,2.5,2)
intd_SF_PowerL = grndm.intd_random_net(SF_PowerL_a,SF_PowerL_b)

print(len(intd_SF_PowerL.nodes()))
grndm.intdNetworkDraw(intd_SF_PowerL)
# %%
# 3-1 SF_PowerL Attacked
intd_SF_PowerL_attck = cas.attack_network(intd_SF_PowerL, SF_PowerL_a, SF_PowerL_b, 0.8)

print(len(intd_SF_PowerL_attck.nodes()))
grndm.intdNetworkDraw(intd_SF_PowerL_attck)
print(":)")
# %%
