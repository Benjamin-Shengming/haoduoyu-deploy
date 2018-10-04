#!/usr/bin/python

import subprocess
import os
import sys
import shutil
import argparse
# check sudo user
#
this_module = sys.modules[__name__]


def install_pre_requirest():
    # install python pip as first step
    subprocess.check_call(['rm', "/usr/bin/python"])
    subprocess.check_call(['ln', "-s", "/usr/bin/python3", "/usr/bin/python"])
    subprocess.check_call(['apt', "install", "python3-pip", "-y"])
    subprocess.check_call(['apt', "update", "-y"])
    subprocess.check_call(['pip3', "install", "fabric"])


def check_run_as_root():
    if os.geteuid() != 0:
        raise ValueError("Please run this script as root(sudo)!")


def pip_install(pkg):
    from invoke import run
    run("pip3 install {}".format(pkg))


def apt_install(pkg):
    from invoke import run
    run("apt install {}".format(pkg))


def git_clone(repo_url):
    from invoke import run
    run("git clone {}".format(repo_url))


git_repos = [
    r"https://github.com/Benjamin-Shengming/localstorage-writer.git",
    r"https://github.com/Benjamin-Shengming/localstorage-reader.git",
    r"https://github.com/Benjamin-Shengming/autolink.git",
    r"https://github.com/plotly/dash-table-experiments.git",

    # major repo
    r"https://github.com/Benjamin-Shengming/flask-vue-club.git",
]
# folders to build/clean
build_repos_dir = [
    "localstorage-writer",
    "localstorage-reader",
    "autolink",
    "dash-table-experiments",
    "flask-vue-club",
]


def install_apt_packages():
    # install apt package
    apt_packages = [
        'npm',
    ]
    for item in apt_packages:
        apt_install(item)


def clean_repos(repos):
    for folder in repos:
        if os.path.exists(folder):
            shutil.rmtree(folder)


def install_python_packages():
    # install python package
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
        "cherrypy",
        "wechatpy",
        "sqlalchemy",
        "flask_login",
        "flask_babel",
        "Pillow",
        "pyjwt",

    ]
    for item in python_packages:
        pip_install(item)


def clone_repos(repos):
    for item in repos:
        git_clone(item)


def build_repos(repos):
    from invoke import context
    # build repos
    for repo in repos:
        c = context.Context()
        if repo != "flask-vue-club":
            with c.cd(repo):
                c.run("npm install")
                try:
                    c.run("npm run prepublish")
                except Exception as e:
                    print(str(e))
                c.run("npm run install-local")


# command can be invoke from command line interface
def run_install_python_package(args):
    install_python_packages()


def run_install_apt_pkg(args):
    install_apt_packages()


def run_build_repo(args):
    build_repos(build_repos_dir)


def run_clean_repo(args):
    clean_repos(build_repos_dir)


def run_clone_git_repos(args):
    clone_repos(git_repos)


def run_all(args):
    run_install_apt_pkg(args)
    run_install_python_package(args)
    run_clean_repo(args)
    run_clone_git_repos(args)
    run_build_repo(args)


def available_commands():
    run_commands = [item for item in dir(this_module)
                    if item.startswith("run_")]
    # replace understore to hyphen
    return [item.replace("_", "-") for item in run_commands]


def call_command(command_str, args):
    func_to_call = getattr(this_module, command_str.replace("-", "_"))
    return func_to_call(args)


def parse_args():
    parser = argparse.ArgumentParser(description='Arguments for deployment.')

    parser.add_argument('-c', "--command",
                        help="choose which command to run, default run-all," +
                        str(available_commands()),
                        default='run-all')

    args = parser.parse_args()
    if args.command not in available_commands():
        parser.print_help()
        sys.exit(-1)
    return args


def main():
    args = parse_args()
    check_run_as_root()
    install_pre_requirest()
    call_command(args.command, args)


if __name__ == "__main__":
    main()
