import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    persons = orders.merge(
        company[company["name"] == "RED"],
        left_on="com_id",
        right_on="com_id"
    )["sales_id"].unique()

    return sales_person[~sales_person["sales_id"].isin(persons)][["name"]]