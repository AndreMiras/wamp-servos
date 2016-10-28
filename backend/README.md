# Backend

This is the backend part e.g. running on a Raspberry Pi.


## Install
```
sudo apt install libpython-dev libffi-dev libssl-dev
pip install -r requirements.txt
```

## Run
```
AUTOBAHN_DEMO_ROUTER=wss://demo.crossbar.io/ws python backend.py
```
