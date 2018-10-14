#!/bin/sh

#==============================================================
# yum installation

#install ius release
yum install -y https://centos6.iuscommunity.org/ius-release.rpm
yum -y update
yum -y install fontconfig freetype freetype-devel fontconfig-devel libstdc++
yum -y install bzip2 
## install yum replace plugin
yum -y install yum-plugin-replace

## install python 3
yum -y install python36u python36u-libs python36u-devel python36u-pip python36u-devel python36u-gunicorn python36u-lxml python36u-setproctitle python36u-setuptools python36u-test python36u-tkinter python36u-tools 
## install git
yum -y install git2u-all

## install node js
curl --silent --location https://rpm.nodesource.com/setup_10.x | sudo bash -
yum -y install nodejs

# temporarily link to python3
rm /usr/bin/python
ln -s /usr/bin/python3.6 /usr/bin/python

ln -s /usr/bin/pip3.6 /usr/bin/pip3
ln -s /usr/bin/python3.6 /usr/bin/python3

pip3 install fabric
pip3 install pyinvoke 

#=============================================================
python3 deploy.py

rm /usr/bin/python
ln -s /usr/bin/python2.6 /usr/bin/python
