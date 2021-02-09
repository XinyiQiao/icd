# -*- coding: utf-8 -*-

'''
cli
---

console script for icd.
'''


import click
import sys
import os
import pathlib
import pandas as pd
from .icd import process

@click.group()
def main():
    pass

@main.command()
@click.argument('data_dir')
@click.option('--output', '-o', help = "Output directory.")
def preprocess(data_dir, output):
    click.echo("preprocessing!")
    # check existing directories and make all necessary directories
    data_dir = pathlib.Path(data_dir)
    if not os.path.isdir(data_dir):
        click.echo(f"Error: {data_dir} is not a directory")
        sys.exit(1)
    if output is None:
        output_dir = data_dir/"output" # use default
    else:
        output_dir = pathlib.Path(output)
    os.makedirs(output_dir)

    admissions = process(data_dir)
    os.chdir(output_dir)
    admissions.to_csv("output.csv", index=False)

def entry_point():
    '''
    required to make setuptools and click play nicely (context object)
    '''

    return sys.exit(main())  # add obj={} to create in context


if __name__ == "__main__":
    entry_point()
