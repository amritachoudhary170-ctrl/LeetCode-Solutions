import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    counts = employee.groupby("managerId").size()
    managers = counts[counts >= 5].index
    return employee[employee["id"].isin(managers)][["name"]]