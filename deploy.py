#!/usr/bin/python

import subprocess
import os
import sys
import shutil
# check sudo user
#

if os.getuid() != 0:
    raise ValueError("please run: sudo ./deploy.py")

# install python pip as first step
subprocess.check_call(['apt', "install", "python3-pip"])
subprocess.check_call(['apt', "update"])

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



#install sh library
try:
    import fabric
except:
    install_pkg('fabric')

from invoke import run, context

def pip_install(pkg):
    run("pip install {}".format(pkg))


def apt_install(pkg):
    run("apt install {}".format(pkg))

def git_clone(repo_url):
    run("git clone {}".format(repo_url))

# folders to delete
build_repos = [
    "localstorage-writer",
    "localstorage-reader",
    "autolink",
    "dash-table-experiments",
    "flask-vue-club",
]

for folder in build_repos:
    if os.path.exists(folder):
        shutil.rmtree(folder)

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
    r"https://github.com/Benjamin-Shengming/localstorage-writer.git",
    r"https://github.com/Benjamin-Shengming/localstorage-reader.git",
    r"https://github.com/Benjamin-Shengming/autolink.git",
    r"https://github.com/plotly/dash-table-experiments.git",

    # major repo
    r"https://github.com/Benjamin-Shengming/flask-vue-club.git",

]
for item in git_repos:
    git_clone(item)

# build repos
for repo in build_repos:
    c = context.Context()
    if repo != "flask-vue-club":
        with c.cd(repo):
            c.run("npm install")
            #c.run("npm run prepublish")
            c.run("npm run install-local")


