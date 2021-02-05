# -*- coding: utf-8 -*-

"""Main module."""

import pandas as pd

def process(input_dir):
    # read in data
    admissions = pd.read_csv(input_dir/"ADMISSIONS.csv")
    procedures_icd = pd.read_csv(input_dir/"PROCEDURES_ICD.csv")
    diagnoses_icd = pd.read_csv(input_dir/"DIAGNOSES_ICD.csv")
    patients = pd.read_csv(input_dir/"PATIENTS.csv")
    icu = pd.read_csv(input_dir/"ICUSTAYS.csv")
    services = pd.read_csv(input_dir/"SERVICES.csv")
    transfers = pd.read_csv(input_dir/"TRANSGERS.csv")

    # PROCSDURES_ICD
    procedures_icd.rename(columns={"ICD9_CODE":"ICD9_Procedures"})
    procedures_icd = procedures_icd[['HADM_ID','ICD9_Procedures']]
    admissions.merge(procedures_icd, how = "left", on="HADM_ID")

    # DIAGNOSES_ICD
    diagnoses_icd.rename(columns={"ICD9_CODE":"ICD9_Diagnoses"})
    diagnoses_icd = diagnoses_icd[['HADM_ID','ICD9_Diagnoses']]
    admissions.merge(diagnoses_icd, how = "left", on="HADM_ID")
    
    # PATIENTS
    patients = patients[['SUBJECT_ID','GENDER', 'DOB','DOD','DOD_HOSP']]
    admissions.merge(patients, how = "left", on = "SUBJECT_ID")

    # ICUSTAYS
    icu = icu[['HADM_ID','ICUSTAY_ID','INTIME','OUTTIME','LOS']]
    admissions.merge(icu, how = "left", on = "HADM_ID")

    # SERVICES
    services = services[['HADM_ID','TRANSFERTIME','PREV_SERVICE','CURR_SERVICE']]
    admissions.join(services, how = "left", on = "HADM_ID")

    return admissions