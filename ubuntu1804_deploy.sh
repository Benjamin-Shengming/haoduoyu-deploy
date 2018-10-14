#!/usr/bin/sh

#==============================================================
# apt installation
apt install python3-pip -y
apt update -pip -y
pip3 install fabric
pip3 install pyinvoke 

#=============================================================
python3 deploy.py

