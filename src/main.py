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
