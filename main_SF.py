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
    # print("\n++++++++++++++++++++++++++++++")
    # print("SF N2000 gamma 2.7 Test Start...")
    # print("++++++++++++++++++++++++++++++\n")

    # gPaths = ['data/pickle/SF/SFn2000_27_a.gpickle',
    #         'data/pickle/SF/SFn2000_27_b.gpickle',
    #         'data/pickle/SF/int_SFn2000_27.gpickle']
    # SFn2000_27 = generate_pinf_SF(t=10, hasGraph=True, files = gPaths)
    # np.savetxt('./notebooks/results/1012/SFn2000_27.csv', SFn2000_27, delimiter=',')

    # print("\n++++++++++++++++++++++++++++++")
    # print("SF N2000 gamma 3.0 Test Start...")
    # print("++++++++++++++++++++++++++++++\n")

    # gPaths = ['data/pickle/SF/SFn2000_30_a.gpickle',
    #         'data/pickle/SF/SFn2000_30_b.gpickle',
    #         'data/pickle/SF/int_SFn2000_30.gpickle']
    # SFn2000_30 = generate_pinf_SF(t=10, hasGraph=True, files = gPaths)
    # np.savetxt('./notebooks/results/1012/SFn2000_30.csv', SFn2000_30, delimiter=',')

    print("\n++++++++++++++++++++++++++++++")
    print("SF N%d gamma %f <k> = %f Graph Generte..." %(n,g,k))
    print("++++++++++++++++++++++++++++++\n")

    SFn_a = networkSF_w_3Dpos_PowerL(n,g,k,1)
    filepath = "data/pickle/SF/SFn"+str(n)+"_"+str(int(g*10))+"_a.gpickle"
    nx.write_gpickle(SFn_a, filepath)
    print("SF N%d gamma %f <k> = %f A Graph Done..." %(n,g,k))
    print(filepath+"\n")

    SFn_b = networkSF_w_3Dpos_PowerL(n,g,k,2)
    filepath = "data/pickle/SF/SFn"+str(n)+"_"+str(int(g*10))+"_b.gpickle"
    nx.write_gpickle(SFn_b, filepath)
    print("SF N%d gamma %f <k> = %f B Graph Done..." %(n,g,k))
    print(filepath+"\n")


    intd_SF = intd_random_net(SFn_a,SFn_b)
    filepath = "data/pickle/SF/int_SFn"+str(n)+"_"+str(int(g*10))+".gpickle"
    nx.write_gpickle(intd_SF, filepath)
    print("intd SF N%d gamma %f <k> = %f B Graph Done..." %(n,g,k))
    print(filepath+"\n")



    # print("\n++++++++++++++++++++++++++++++")
    # print("SF N50000 gamma 2.7 <k> = 4 Graph Generte...")
    # print("++++++++++++++++++++++++++++++\n")

    # start = datetime.now()
    # SFn50000_27_a = networkSF_w_3Dpos_PowerL(50000,2.7,4,1)
    # nx.write_gpickle(SFn50000_27_a, "../data/pickle/SF/SFn50000_27_a.gpickle")
    # time = datetime.now() - start
    # print("...SFn50000_27_a Graph Generate Done!", time)

    # start = datetime.now()
    # SFn50000_27_b = networkSF_w_3Dpos_PowerL(50000,2.7,4,1)
    # nx.write_gpickle(SFn50000_27_b, "../data/pickle/SF/SFn50000_27_b.gpickle")
    # time = datetime.now() - start
    # print("...SFn50000_27_b Graph Generate Done!", time)


    # print("\n++++++++++++++++++++++++++++++")
    # print("SF N50000 gamma 2.3 <k> = 4 Graph Generte...")
    # print("++++++++++++++++++++++++++++++\n")

    # start = datetime.now()
    # SFn50000_23_a = networkSF_w_3Dpos_PowerL(50000,2.3,4,1)
    # nx.write_gpickle(SFn50000_23_a, "../data/pickle/SF/SFn50000_23_a.gpickle")
    # time = datetime.now() - start
    # print("...SFn50000_23_a Graph Generate Done!", time)

    # start = datetime.now()
    # SFn50000_23_b = networkSF_w_3Dpos_PowerL(50000,2.3,4,2)
    # nx.write_gpickle(SFn50000_23_b, "../data/pickle/SF/SFn50000_23_b.gpickle")
    # time = datetime.now() - start
    # print("...SFn50000_23_b Graph Generate Done!", time)

    # print("\n++++++++++++++++++++++++++++++")
    # print("SF N2000 gamma 2.5 Test Start...")
    # print("++++++++++++++++++++++++++++++\n")

    # SFn2000_25 = generate_pinf_SF(2000, 2.5, 10)
    # np.savetxt('./notebooks/results/1012/SFn2000_25.csv', SFn2000_25, delimiter=',')



if __name__ == "__main__":
    main()