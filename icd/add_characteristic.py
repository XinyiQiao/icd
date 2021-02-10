def add_age(admissions):
    admissions.INTIME = pd.to_datetime(admissions.INTIME).dt.date
    admissions.DOB = pd.to_datetime(admissions.DOB).dt.date
    admissions['AGE'] = admissions.apply(lambda e: (e.INTIME - e.DOB).days/365, axis=1)
    admissions.loc[admissions.AGE < 0, 'AGE'] = 90
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