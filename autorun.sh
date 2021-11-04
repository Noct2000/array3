#!/usr/bin/bash

sudo apt install -y python3 python3-pip python3-venv
python3 -m venv env
source env/bin/activate
python main.py
deactivate
