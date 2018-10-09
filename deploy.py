#!/usr/bin/python3

import subprocess
import os
import sys
import shutil
import argparse
# check sudo user
#
this_module = sys.modules[__name__]



def check_run_as_root():
    if os.geteuid() != 0:
        raise ValueError("Please run this script as root(sudo)!")

def git_clone(repo_url):
    from invoke import run
    run("git clone {}".format(repo_url))


git_repos = [
    r"https://github.com/Benjamin-Shengming/localstorage-writer.git",
    r"https://github.com/Benjamin-Shengming/localstorage-reader.git",
    r"https://github.com/Benjamin-Shengming/autolink.git",
    r"https://github.com/plotly/dash-table-experiments.git",

    # major repo
    r"https://github.com/Benjamin-Shengming/haoduoyu-club.git",
]

# folders to build
build_repos_dir = [
    "localstorage-writer",
    "localstorage-reader",
    "autolink",
    "dash-table-experiments",
    "haoduoyu-club"
]



def clean_repos(repos):
    for folder in repos:
        if os.path.exists(folder):
            shutil.rmtree(folder)


def clone_repos(repos):
    for item in repos:
        git_clone(item)


def build_repos(repos):
    from invoke import context
    # build repos
    for repo in repos:

        c = context.Context()
        with c.cd(repo):
            if repo == "haoduoyu-club":
                c.run("pip3 install -r requirement.txt")
            else:
                c.run("npm install")
                try:
                    c.run("npm run prepublish")
                except Exception as e:
                    print(str(e))
                c.run("npm run install-local")



def run_build_repo(args):
    build_repos(build_repos_dir)


def run_clean_repo(args):
    clean_repos(build_repos_dir)


def run_clone_repos(args):
    clone_repos(git_repos)


def run_all(args):
    run_clean_repo(args)
    run_clone_repos(args)
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
    call_command(args.command, args)


if __name__ == "__main__":
    main()
