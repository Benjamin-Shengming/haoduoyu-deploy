#!/usr/bin/python

import subprocess
import os
import sys
# check sudo user

if os.getuid() != 0:
    raise ValueError("please run: sudo ./deploy.py")

# install python pip as first step
subprocess.run(['apt', "install", "python-pip"])

try:
    import pip
except:
    raise ValueError("Pip was not installed!")

def install_pkg(package):
    ret = pip.main(['install', package])
    print(ret)

#install sh library
try:
    import sh
except:
    install_pkg('sh')


from sh import pip, apt, git, npm

def pip_install(pkg):
    for line in pip("install", pkg, _iter=True):
        sys.stdout.write(line)


def apt_install(pkg):
    for line in apt("install", pkg, _iter=True):
        sys.stdout.write(line)

# install apt package
apt_install('npm')

#install python package
pip_install("dash")
pip_install("dash-html-components")
pip_install("dash-core-components")
pip_install("requests")

#git clone
