from src.attack import *
from src.create import *
from src.measure import *

print("\n++++++++++++++++++++++++++++++")
print("SF N2000 gamma 2.5 Test Start...")
print("++++++++++++++++++++++++++++++\n")

SFn2000_25 = generate_pinf_SF(2000, 2.5, 10)
np.savetxt('./notebooks/results/1012/SFn2000_25.csv', SFn2000_25, delimiter=',')

print("\n++++++++++++++++++++++++++++++")
print("SF N2000 gamma 2.7 Test Start...")
print("++++++++++++++++++++++++++++++\n")

SFn2000_27 = generate_pinf_SF(2000, 2.7, 10)
np.savetxt('./notebooks/results/1012/SFn2000_27.csv', SFn2000_27, delimiter=',')

print("\n++++++++++++++++++++++++++++++")
print("SF N2000 gamma 3.0 Test Start...")
print("++++++++++++++++++++++++++++++\n")

SFn2000_30 = generate_pinf_SF(2000, 3, 10)
np.savetxt('./notebooks/results/1012/SFn2000_30.csv', SFn2000_30, delimiter=',')