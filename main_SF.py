from src.attack import *
from src.create import *
from src.measure import *
from datetime import datetime

print("\n++++++++++++++++++++++++++++++")
print("SF N2000 gamma 2.7 Test Start...")
print("++++++++++++++++++++++++++++++\n")

gPaths = ['data/pickle/SF/SFn2000_27_a.gpickle',
        'data/pickle/SF/SFn2000_27_b.gpickle',
        'data/pickle/SF/int_SFn2000_27.gpickle']
SFn2000_27 = generate_pinf_SF(t=10, hasGraph=True, files = gPaths)
np.savetxt('./notebooks/results/1012/SFn2000_27.csv', SFn2000_27, delimiter=',')

print("\n++++++++++++++++++++++++++++++")
print("SF N2000 gamma 3.0 Test Start...")
print("++++++++++++++++++++++++++++++\n")

gPaths = ['data/pickle/SF/SFn2000_30_a.gpickle',
        'data/pickle/SF/SFn2000_30_b.gpickle',
        'data/pickle/SF/int_SFn2000_30.gpickle']
SFn2000_30 = generate_pinf_SF(t=10, hasGraph=True, files = gPaths)
np.savetxt('./notebooks/results/1012/SFn2000_30.csv', SFn2000_30, delimiter=',')


print("\n++++++++++++++++++++++++++++++")
print("SF N2000 gamma 2.5 Graph Generte...")
print("++++++++++++++++++++++++++++++\n")

start = datetime.now()
SFn2000_25_a = networkSF_w_3Dpos_PowerL(2000,2.5,1)
nx.write_gpickle(SFn2000_25_a, "../data/pickle/SF/SFn2000_25_a.gpickle")
time = datetime.now() - start
print("...SFn2000_25_a Graph Generate Done!", time)

start = datetime.now()
SFn2000_25_b = networkSF_w_3Dpos_PowerL(2000,2.5,2)
nx.write_gpickle(SFn2000_25_b, "../data/pickle/SF/SFn2000_25_b.gpickle")
time = datetime.now() - start
print("...SFn2000_25_b Graph Generate Done!", time)

start = datetime.now()
int_SFn2000_25 = intd_random_net(SFn2000_25_a,SFn2000_25_b)
nx.write_gpickle(int_SFn2000_25, "../data/pickle/SF/int_SFn2000_25.gpickle")
time = datetime.now() - start
print("...int_SFn2000_25 Graph Generate Done!", time)


# print("\n++++++++++++++++++++++++++++++")
# print("SF N2000 gamma 2.5 Test Start...")
# print("++++++++++++++++++++++++++++++\n")

# SFn2000_25 = generate_pinf_SF(2000, 2.5, 10)
# np.savetxt('./notebooks/results/1012/SFn2000_25.csv', SFn2000_25, delimiter=',')