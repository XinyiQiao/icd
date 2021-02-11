import pandas as pd

def add_age(admissions):   
    INTIME = pd.to_datetime(admissions.INTIME).dt.date
    DOB = pd.to_datetime(admissions.DOB).dt.date
    age = [pd.NaT]*len(admissions)
    for i in range(0, len(admissions)):
        if pd.isnull(INTIME[i])==True or pd.isnull(DOB[i])==True:
            age[i] = pd.NaT
        else:
            age[i] = (INTIME[i]-DOB[i]).days // 365
    admissions['AGE'] = pd.DataFrame(data=age)
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