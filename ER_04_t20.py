from src.measure import *

print("\n++++++++++++++++++++++++++++++")
print("ER N4000 Test Start...")
print("++++++++++++++++++++++++++++++\n")

ERn4000k4_20 = generate_pinf_ER(4000, 4, 10)
np.savetxt('./notebooks/results/ER/t20/ERn4000t20.csv', ERn4000k4_20, delimiter=',')