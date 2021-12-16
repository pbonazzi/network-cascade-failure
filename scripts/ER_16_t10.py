from src.measure import *

print("\n++++++++++++++++++++++++++++++")
print("ER N16000 Test Start...")
print("++++++++++++++++++++++++++++++\n")

ERn16000k4 = generate_pinf_ER(16000, 4, 10)
np.savetxt('./notebooks/results/ER/t10/ERn16000k4.csv', ERn16000k4, delimiter=',')
