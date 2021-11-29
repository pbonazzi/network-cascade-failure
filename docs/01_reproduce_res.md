# Reproducibility

### 1. Clone the repository

```
git clone https://github.com/pbonazzi/21-11-network-cascade-failure.git
cd 21-11-network-cascade-failure
```

### 2. Set up the environment 

Linux/macOS
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Windows
```
virtualenv --python C:\Path\To\Python\python.exe venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run experiment

```
python3 src/main.py
```


#### [optional] Download the dataset

To get the original dataset run :

```
git clone https://github.com/ComplexNetTSP/MultilayerParis.git
```

For other network datasets click [here](https://icon.colorado.edu/#!/networks) .