from src.measure import *

print("\n++++++++++++++++++++++++++++++")
print("ER N64000 Test Start...")
print("++++++++++++++++++++++++++++++\n")

ERn64000k4 = generate_pinf_ER(64000, 4, 10)
np.savetxt('./notebooks/results/ER/t10/ERn64000k4.csv', ERn64000k4, delimiter=',')