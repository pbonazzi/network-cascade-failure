# %%
import sys
import networkx as nx
from matplotlib import pyplot as plt
import numpy as np
import json

# %%

import generation as rndm
import cascadeflr as cas

# %%
N, n1, n2 = rndm.new_network(5, 3)
A = cas.attack_network(N, n1, n2, 0.8)

print(":)")
