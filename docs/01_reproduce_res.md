# Reproducibility

### 1. Clone the repository

```
git clone https://github.com/pbonazzi/21-11-network-cascade-failure.git
cd 21-network-cascade-failure
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

### 3. Import virtual environment in Jupyter Notebook

```
python -m ipykernel install --name=myenv
```

### 4. Run the experiments

Select any experiments [here](../notebooks) .

### 5. Uninstall the virtual environment in Jupyter Notebook

```
jupyter kernelspec list
jupyter kernelspec uninstall venv
```
