#!/bin/sh

pip install rich

sudo mkdir -p /opt/watodo/

sudo cp ./watodo.py /opt/watodo/

sudo mv ./watodo /usr/local/bin/
