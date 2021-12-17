from src.measure import *

print("\n++++++++++++++++++++++++++++++")
print("ER N1000 Test Start...")
print("++++++++++++++++++++++++++++++\n")

ERn1000k4_20 = generate_pinf_ER(1000, 4, 20)
np.savetxt('./notebooks/results/ER/t20/ERn1000k4_20.csv', ERn1000k4_20, delimiter=',')