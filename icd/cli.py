# -*- coding: utf-8 -*-

'''
cli
---

console script for icd.
'''


import click
import sys


@click.command()
def main(args=None):
    '''
    icd command line interface
    '''

    click.echo("update icd.cli.main")
    return 0


def entry_point():
    '''
    required to make setuptools and click play nicely (context object)
    '''

    return sys.exit(main())  # add obj={} to create in context


if __name__ == "__main__":
    entry_point()
