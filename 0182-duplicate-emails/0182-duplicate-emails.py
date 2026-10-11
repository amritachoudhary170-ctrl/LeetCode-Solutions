import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    res = person.groupby('email').size().reset_index(name= 'count')

    return res[res['count']>1][['email']]