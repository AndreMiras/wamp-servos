# Backend

The backend is composed of two parts:

 * `libcontroller.py` is a simple "driver" for the [servo conroller](http://letsmakerobots.com/files/32_Servo_Controller_Manual.pdf) board
 * `backend.py` is responsible for exposing the `libcontroller.py` using WAMP Remote Procedure Call.

The backend must be connected to the servo controller board.

## Install
```
sudo apt install libpython-dev libffi-dev libssl-dev
pip install -r requirements.txt
```

## Run
```
AUTOBAHN_DEMO_ROUTER=wss://demo.crossbar.io/ws python backend.py
```
