# Welcome to network cascade failure

Modern systems are  increasingly  coupled  together and interdependent. For example, train and metro networks are interdependent networks in destination planning problems.

<p align="center">
  <img width="auto" height="auto" src="https://github.com/pbonazzi/21-network-cascade-failure/blob/main/notebooks/figure/PARIS/metro_train.png?style=centerme">
</p>

Following the approach presented in (Sergey V Buldyrev et al. 2010a), we simulate a cascade of failures on synthetic random Erdos–Renyi IN, Scale-free IN, and a real world IN : the Paris Multilayer Transport Network (Asgari et al. 2016). 

## 1. Reproducibility

[Follow these instructions](./docs/01_reproduce_res.md) to set up a local repo and the environment.

## 2. Citation 

Eleonora Pura, 17-732-678
Hyeongkyun Kim 21-732-797
Pietro Bonazzi 17-200-635
Songyi Han 18-796-847

:page_with_curl: Paper [on Github](./docs/reports/report.pdf)    
:pencil: Presentation [on Github](./docs/reports/presentation.pdf)

```
@article{uzh2021transp,
  title={Catastrophic cascade of failures in interdependent networks},
  author={Bonazzi, Han, Kim and Pura},
  year={2021}
}
```

#  3. Reference

To get the Paris dataset run :

```
git clone https://github.com/ComplexNetTSP/MultilayerParis.git
```

For other network datasets click [here](https://icon.colorado.edu/#!/networks) .
