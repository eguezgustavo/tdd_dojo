#! /usr/bin/env python

import os
import json
import signal
import subprocess

import click

import sys
from os.path import dirname
sys.path.append("./example_4/api/application")

docker_compose_file = "docker/development.yml"
docker_compose_cmdline = ["docker-compose", "-f", docker_compose_file]


@click.group()
def cli():
    pass


@cli.command(context_settings={"ignore_unknown_options": True})
@click.argument("subcommand", nargs=-1, type=click.Path())
def test(subcommand):
    cmdline = ["pytest","-svv"] + list(subcommand)

    try:
        p = subprocess.Popen(cmdline)
        p.wait()
    except KeyboardInterrupt:
        p.send_signal(signal.SIGINT)
        p.wait()


@cli.command(context_settings={"ignore_unknown_options": True})
@click.argument("subcommand", nargs=-1, type=click.Path())
def compose(subcommand):
    cmdline = docker_compose_cmdline + list(subcommand)

    try:
        print(cmdline)
        p = subprocess.Popen(cmdline)
        p.wait()
    except KeyboardInterrupt:
        p.send_signal(signal.SIGINT)
        p.wait()


if __name__ == "__main__":
    cli()