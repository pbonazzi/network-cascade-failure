from src.attack import *
from src.create import *
from src.measure import *
from datetime import datetime

import click


@click.command()
@click.option('--n', type=int, default = 20)
@click.option('--g', type=float, default = 3)
@click.option('--k', type=float, default = 4)


def main(n, g, k):
    file_a = "data/pickle/SF/SFn"+str(n)+"_"+str(int(g*10))+"_k"+str(int(k))+"_a.gpickle"
    file_b = "data/pickle/SF/SFn"+str(n)+"_"+str(int(g*10))+"_k"+str(int(k))+"_b.gpickle"
    file_intd = "data/pickle/SF/int_SFn"+str(n)+"_"+str(int(g*10))+"_k"+str(int(k))+".gpickle"

    print("\n++++++++++++++++++++++++++++++")
    print("SF N2000 gamma 2.7 Test Start...")
    print("++++++++++++++++++++++++++++++\n")

    gPaths = [file_a,file_b,file_intd]
    SFn2000_27 = generate_pinf_SF(t=10, hasGraph=True, files = gPaths)
    filepath = "notebooks/results/SF/SFn"+str(n)+"_"+str(int(g*10))+"_k"+str(int(k))+"_a.gpickle"
    np.savetxt('./notebooks/results/1012/SFn2000_27.csv', SFn2000_27, delimiter=',')

    # print("\n++++++++++++++++++++++++++++++")
    # print("v1.0 SF N%d gamma %f <k> = %f Graph Generate..." %(n,g,k))
    # print("++++++++++++++++++++++++++++++\n")

    # SFn_a = networkSF_w_3Dpos_PowerL(n,g,k,1)
    # filepath = "data/pickle/SF/SFn"+str(n)+"_"+str(int(g*10))+"_k"+str(int(k))+"_a.gpickle"
    # nx.write_gpickle(SFn_a, filepath)
    # print("SF N%d gamma %f <k> = %f A Graph Done..." %(n,g,k))
    # print(filepath+"\n")

    # SFn_b = networkSF_w_3Dpos_PowerL(n,g,k,2)
    # filepath = "data/pickle/SF/SFn"+str(n)+"_"+str(int(g*10))+"_k"+str(int(k))+"_b.gpickle"
    # nx.write_gpickle(SFn_b, filepath)
    # print("SF N%d gamma %f <k> = %f B Graph Done..." %(n,g,k))
    # print(filepath+"\n")


    # intd_SF = intd_random_net(SFn_a,SFn_b)
    # filepath = "data/pickle/SF/int_SFn"+str(n)+"_"+str(int(g*10))+"_k"+str(int(k))+".gpickle"
    # nx.write_gpickle(intd_SF, filepath)
    # print("intd SF N%d gamma %f <k> = %f B Graph Done..." %(n,g,k))
    # print(filepath+"\n")



if __name__ == "__main__":
    main()