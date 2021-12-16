from src.measure import *

print("\n++++++++++++++++++++++++++++++")
print("ER N4000 Test Start...")
print("++++++++++++++++++++++++++++++\n")

ERn4000k4_50 = generate_pinf_ER(4000, 4, 50)
np.savetxt('./notebooks/results/ER/t50/ERn4000k4_50.csv', ERn4000k4_50, delimiter=',')