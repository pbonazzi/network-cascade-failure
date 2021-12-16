from src.measure import *

print("\n++++++++++++++++++++++++++++++")
print("ER N1000 Test Start...")
print("++++++++++++++++++++++++++++++\n")

ERn1000k4 = generate_pinf_ER(1000, 4, 50)
np.savetxt('./notebooks/results/ER/t50/ERn1000k4_50.csv', ERn1000k4, delimiter=',')