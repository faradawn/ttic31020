# ttic31020

## Install Python Venv
```
# download virtualenv
python3 -m pip install --user virtualenv 

# create a env
python3 -m venv env
source env/bin/activate

# install packages
pip install --upgrade pip
pip install numpy

# install with requirements.txt
pip install -r requirements.txt
```

## SSH Jupyter Notebook
```
ipython kernel install --user --name=venv

pip install jupyter 
jupyter notebook --no-browser --port=8888

# localhost
ssh -i ~/.ssh/chameleon-1.pem -NL localhost:1234:localhost:8888 cc29.114.109.75
```