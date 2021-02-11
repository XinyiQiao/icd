import pandas as pd

def add_age(admissions):
    admissions['INTIME']= pd.to_datetime(admissions['INTIME']).dt.year
    admissions['DOB']= pd.to_datetime(admissions['DOB']).dt.year
    admissions['AGE']=admissions['INTIME']-admissions['DOB']
    return admissions
'''
def add_inhospital_mortality_to_admissions(admissions):
    mortality = admissions.DOD.notnull() & ((admissions.ADMITTIME <= admissions.DOD) & (admissions.DISCHTIME >= admissions.DOD))
    mortality = mortality | (admissions.DEATHTIME.notnull() & ((admissions.ADMITTIME <= admissions.DEATHTIME) & (admissions.DISCHTIME >= admissions.DEATHTIME)))
    admissions['MORTALITY'] = mortality.astype(int)
    admissions['MORTALITY_INHOSPITAL'] = admissions['MORTALITY']
    return admissions

def add_inunit_mortality_to_admissionsadmissions(admissions):
    mortality = admissions.DOD.notnull() & ((admissions.INTIME <= admissions.DOD) & (admissions.OUTTIME >= admissions.DOD))
    mortality = mortality | (admissions.DEATHTIME.notnull() & ((admissions.INTIME <= admissions.DEATHTIME) & (admissions.OUTTIME >= admissions.DEATHTIME)))
    admissions['MORTALITY_INUNIT'] = mortality.astype(int)
    return admissions
'''