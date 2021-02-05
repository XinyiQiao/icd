# -*- coding: utf-8 -*-

"""Main module."""

import pandas as pd

def process(input_dir):
    # read in data
    admission = pd.read_csv(input_dir/"ADMISSIONS.csv")
    procedures_icd = pd.read_csv(input_dir/"PROCEDURES_ICD.csv")
    diagnoses_icd = pd.read_csv(input_dir/"DIAGNOSES_ICD.csv")
    
    procedures_icd = procedures_icd[['SUBJECT_ID','HADM_ID','ICD9_CODE']]
    admission.join(procedures_icd, on="HADM_ID")
    diagnoses_icd = diagnoses_icd[['SUBJECT_ID','HADM_ID','ICD9_CODE']]
    admission.join(diagnoses_icd, on="HADM_ID")
    return admission