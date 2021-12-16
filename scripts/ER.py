import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from src.attack import *
from src.create import *
from src.measure import *
from datetime import datetime

import click


@click.command()
@click.option('--n', type=int, default = 20)
@click.option('--k', type=float, default = 4)
@click.option('--test', type=bool, default = False)
@click.option('--t', type=int, default = 10)

def main(n, k, test, t):
    if test:
        file_a = "../data/pickle/ER/ERn"+str(n)+"_k"+str(int(k))+"_a.gpickle"
        file_b = "../data/pickle/ER/ERn"+str(n)+"_k"+str(int(k))+"_b.gpickle"
        file_intd = "../data/pickle/ER/int_ERn"+str(n)+"_k"+str(int(k))+".gpickle"

        print("\n++++++++++++++++++++++++++++++")
        print("v1.0 ER N%d <k> = %f Graph Cascade Test..." %(n,k))
        print("++++++++++++++++++++++++++++++\n")

        gPaths = [file_a,file_b,file_intd]
        result = generate_pinf_ER(n=0, k=0, t=t, hasGraph=True, files = gPaths)
        filepath = "../notebooks/results/ERn"+str(n)+"_k"+str(int(k))+".csv"
        np.savetxt(filepath, result, delimiter=',')
    
    else:

        print("\n++++++++++++++++++++++++++++++")
        print("v1.0 ER N%d <k> = %f Graph Generate..." %(n,k))
        print("++++++++++++++++++++++++++++++\n")

        ERn_a = networkER_w_3Dpos(n,k,1)
        filepath = "../data/pickle/ER/ERn"+str(n)+"_k"+str(int(k))+"_a.gpickle"
        nx.write_gpickle(ERn_a, filepath)
        print("ER N%d <k> = %f A Graph Done..." %(n,k))
        print(filepath+"\n")

        ERn_b = networkER_w_3Dpos(n,k,2)
        filepath = "../data/pickle/ER/ERn"+str(n)+"_k"+str(int(k))+"_b.gpickle"
        nx.write_gpickle(ERn_b, filepath)
        print("ER N%d <k> = %f B Graph Done..." %(n,k))
        print(filepath+"\n")

        intd_ER = intd_random_net(ERn_a,ERn_b)
        filepath = "../data/pickle/ER/int_ERn"+str(n)+"_k"+str(int(k))+".gpickle"
        nx.write_gpickle(intd_ER, filepath)
        print("intd ER N%d <k> = %f B Graph Done..." %(n,k))
        print(filepath+"\n")



if __name__ == "__main__":
    main()