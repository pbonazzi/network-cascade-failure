from src.attack import *
from src.create import *
from src.measure import *

print("\n++++++++++++++++++++++++++++++")
print("ER N1000 Test Start...")
print("++++++++++++++++++++++++++++++\n")

ERn16000k4 = generate_pinf_ER(16000, 4, 10)
np.savetxt('./notebooks/results/1012/ERn16000k4csv', ERn16000k4, delimiter=',')

print("\n++++++++++++++++++++++++++++++")
print("ER N1000 Test Start...")
print("++++++++++++++++++++++++++++++\n")

ERn32000k4 = generate_pinf_ER(32000, 4, 10)
np.savetxt('./notebooks/results/1012/ERn32000k4.csv', ERn32000k4, delimiter=',')





# #ERn1000k4 = generate_pinf_ER(1000, 4, 10)  # ER model, node=1000, k=4
# np.savetxt('./notebooks/results/0912/ERn1000k4_2.csv', ERn500k4, delimiter=',')
# #np.savetxt('./notebooks/results/0912/ERn1000k4_2.csv', ERn1000k4, delimiter=',')

# ERn1000k4 = np.loadtxt('./notebooks/results/0912/ERn1000k4.csv',delimiter=",")
# #ERn2000k4 = np.loadtxt('./notebooks/results/0912/ERn2000k4.csv',delimiter=",")

# plot_pinf([ERn500k4, ERn1000k4], 4, (2,3), ["ER, n=500, k=4", "ER, n=1000, k=4"], path='./notebooks/results/0912/ERn_inf_500_1000.png', p_theory=True)