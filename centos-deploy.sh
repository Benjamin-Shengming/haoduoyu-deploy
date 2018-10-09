#!/usr/bin/sh

#==============================================================
# yum installation

#install ius release
yum install -y https://centos7.iuscommunity.org/ius-release.rpm
yum update

## install yum replace plugin
yum install yum-plugin-replace

## install python 3
yum install -y python36u python36u-libs python36u-devel python36u-pip

## install git
yum -y install git2u-all

## install node js
curl --silent --location https://rpm.nodesource.com/setup_10.x | sudo bash -
yum -y install nodejs

ln -s /usr/bin/pip3.6 /usr/bin/pip3
ln -s /usr/bin/python3.6 /usr/bin/python3

pip3 install fabric
pip3 install pyinvoke 

#=============================================================
python3 deploy.py


