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

def git_clone(repo_url):
    for line in git("clone", repo_url, _iter=True):
        sys.stdout.write(line)

# install apt package
apt_packages = [
    'npm',
]
for item in apt_packages:
    apt_install(item)

#install python package
python_packages = [
    "dash",
    "dash-html-components",
    "dash-core-components",
    "requests",
    "pandas",
    "plotly",
    "flask",
    "numpy",
    "coloredlogs",
    "python-dateutil",
    "sd-material-ui",
    "imapclient",
]
for item in python_packages:
    pip_install(item)

#git clone
git_repos = [
    r"https://github.com/Benjamin-Shengming/flask-vue-club.git",
    r"https://github.com/Benjamin-Shengming/localstorage-writer.git",
    r"https://github.com/Benjamin-Shengming/localstorage-reader.git",
    r"https://github.com/Benjamin-Shengming/autolink.git",
    r"https://github.com/plotly/dash-table-experiments.git",
]
for item in git_repos:
    git_clone(item)


# build and install repo
build_repos = [
    ""
]
