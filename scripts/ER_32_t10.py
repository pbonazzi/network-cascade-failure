from src.measure import *

print("\n++++++++++++++++++++++++++++++")
print("ER N32000 Test Start...")
print("++++++++++++++++++++++++++++++\n")

ERn32000k4 = generate_pinf_ER(32000, 4, 10)
np.savetxt('./notebooks/results/ER/t10/ERn32000k4.csv', ERn32000k4, delimiter=',')