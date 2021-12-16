from src.measure import *

print("\n++++++++++++++++++++++++++++++")
print("ER N4000 Test Start...sy")
print("++++++++++++++++++++++++++++++\n")

ERn4000k4_20 = generate_pinf_ER(4000, 4, 10)
np.savetxt('./notebooks/results/sy/er/t20/ERn4000t10.csv', ERn4000k4_20, delimiter=',')