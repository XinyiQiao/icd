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
from .clean import (
    icd_clean,
    filter_age,
)

@click.group()
@click.pass_context
@click.argument('data_dir')
def main(ctx, data_dir):
    data_dir = pathlib.Path(data_dir)
    if not os.path.isdir(data_dir):
        click.echo(f"Error: {data_dir} is not a directory")
        sys.exit(1)
    ctx.obj["data_dir"] = data_dir
    if os.path.isdir(data_dir/"output"):
        print(f"Error: output directory already exists")
        sys.exit(1)
    os.makedirs(data_dir/"output")
    

@main.command()
@click.pass_context
def outcome(ctx):
    '''feature and outcome dataframe'''
    # TODO: implement this
    click.echo("TODO:implement")


@main.command()
@click.pass_context
def icdcode(ctx):
    '''icd dataframe'''
    
    diagnoses = filter_age(ctx.obj['data_dir'],"DIAGNOSES_ICD.csv.gz")
    diagnoses = icd_clean(diagnoses)
    compression_opts = dict(method='zip',
                        archive_name='out.csv')
    diagnoses.to_csv(path_or_buf = ctx.obj['data_dir']/"output"/"diagnoses.zip" ,index=False, compression = compression_opts)
    
    procedures = filter_age(ctx.obj['data_dir'],"PROCEDURES_ICD.csv.gz")
    procedures = icd_clean(procedures)
    diagnoses.to_csv(path_or_buf = ctx.obj['data_dir']/"output"/"dignoses.zip" ,index=False, compression = compression_opts)
    #procedures.to_csv(path_or_buf = ctx.obj['data_dir']/"output"/"procedures.csv.zip" ,index=False)


def entry_point():
    '''
    required to make setuptools and click play nicely (context object)
    '''

    return sys.exit(main(obj={}))  # add obj={} to create in context


if __name__ == "__main__":
    entry_point()
