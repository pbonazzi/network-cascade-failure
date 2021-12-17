from src.measure import *

print("\n++++++++++++++++++++++++++++++")
print("ER N2000 Test Start...")
print("++++++++++++++++++++++++++++++\n")

ERn2000k4_20 = generate_pinf_ER(2000, 4, 20)
np.savetxt('./notebooks/results/ER/t20/ERn2000k4_20.csv', ERn2000k4_20, delimiter=',')