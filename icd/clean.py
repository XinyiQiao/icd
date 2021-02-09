# -*- coding: utf-8 -*-

"""Main module."""

import pandas as pd
import numpy as np

def process(input_dir):
    # read in data
    admissions = pd.read_csv(input_dir/"ADMISSIONS.csv.gz")
    procedures_icd = pd.read_csv(input_dir/"PROCEDURES_ICD.csv.gz")
    diagnoses_icd = pd.read_csv(input_dir/"DIAGNOSES_ICD.csv.gz")
    patients = pd.read_csv(input_dir/"PATIENTS.csv.gz")
    icu = pd.read_csv(input_dir/"ICUSTAYS.csv.gz")
    services = pd.read_csv(input_dir/"SERVICES.csv.gz")
    transfers = pd.read_csv(input_dir/"TRANSGERS.csv.gz")
    # admissions = pd.read_csv(input_dir/"ADMISSIONS.csv", compression = 'gzip')

    # PROCSDURES_ICD
    procedures_icd.rename(columns={"ICD9_CODE":"ICD9_Procedures"})
    procedures_icd = procedures_icd[['HADM_ID','ICD9_Procedures']]
    admissions=admissions.merge(procedures_icd, how = "left", on="HADM_ID")

    # DIAGNOSES_ICD
    diagnoses_icd.rename(columns={"ICD9_CODE":"ICD9_Diagnoses"})
    diagnoses_icd = diagnoses_icd[['HADM_ID','ICD9_Diagnoses']]
    admissions=admissions.merge(diagnoses_icd, how = "left", on="HADM_ID")
    
    # PATIENTS
    patients = patients[['SUBJECT_ID','GENDER', 'DOB','DOD','DOD_HOSP']]
    admissions=admissions.merge(patients, how = "left", on = "SUBJECT_ID")

    # ICUSTAYS
    icu = icu[['HADM_ID','ICUSTAY_ID','INTIME','OUTTIME','LOS']]
    admissions=admissions.merge(icu, how = "left", on = "HADM_ID")

    # SERVICES
    services = services[['HADM_ID','TRANSFERTIME','PREV_SERVICE','CURR_SERVICE']]
    admissions=admissions.merge(services, how = "left", on = "HADM_ID")

    # TRANSFERS
    transfers = services[['HADM_ID','INTIME','OUTTIME','LOS']]
    admissions=admissions.merge(transfers, how = "left", on = "HADM_ID")
    return admissions

def icd_clean(input_path):
    # read in data
    df = pd.read_csv(input_path)
    df = df[0:10]
    df = df[['HADM_ID','SUBJECT_ID','ICD9_CODE']]
    df.sort_values(by=['HADM_ID'], inplace=True)
    df.reset_index(inplace=True)
    s = df.pivot_table(index=['HADM_ID'], aggfunc='size')
    max_icd = max(s)
    col_names = ['HADM_ID','SUBJECT_ID']
    for i in range(0, max_icd):
        col_names.append('ICD_'+str(i+1))

    output = pd.DataFrame(
        np.nan, index = range(0, len(s)), 
        columns = col_names
    )
    
    output['HADM_ID']=s.index
    
    i = 0 
    j = 2
    for index, row in df.iterrows():
        if (row['HADM_ID']!=output.iloc[i]['HADM_ID']):
            i += 1
            j = 2
        
        output.iloc[i,1] = row['SUBJECT_ID']
        output.iloc[i,j] = row['ICD9_CODE']
        j += 1
    return output