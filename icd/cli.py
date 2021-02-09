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
from .clean import icd_clean

@click.group()
@click.pass_context()
@click.argument('data_dir')
def main(ctx, data_dir):
    data_dir = pathlib.Path(data_dir)
    if not os.path.isdir(data_dir):
        click.echo(f"Error: {data_dir} is not a directory")
        sys.exit(1)
    ctx.obj["data_dir"] = data_dir 
    os.makedirs(data_dir/"output")
    

@main.command()
@click.pass_context
@click.argument('data_dir')
@click.option('--output', '-o', help = "Output directory.")
def outcome(data_dir, output):
    '''feature and outcome dataframe'''
    # TODO: implement this
    click.echo("TODO:implement")


@main.command()
@click.argument('data_dir')
@click.option('--output','-o', help = "Output directory.")
def icd(data_dir, output):
    '''icd dataframe'''
    output = icd_clean(data_dir/"PROCEDURES_ICD.csv.gz")


def entry_point():
    '''
    required to make setuptools and click play nicely (context object)
    '''

    return sys.exit(main(obj={}))  # add obj={} to create in context


if __name__ == "__main__":
    entry_point()
