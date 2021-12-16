from src.measure import *

print("\n++++++++++++++++++++++++++++++")
print("ER N2000 Test Start...")
print("++++++++++++++++++++++++++++++\n")

ERn2000k4_50 = generate_pinf_ER(2000, 4, 50)
np.savetxt('./notebooks/results/ER/t50/ERn2000k4_50.csv', ERn2000k4_50, delimiter=',')