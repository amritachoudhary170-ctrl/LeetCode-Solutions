import pandas as pd

def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    first_year = sales.groupby('product_id')['year'].min().reset_index().rename(columns={'year': "first_year"})
    res = pd.merge(sales, first_year, left_on=['product_id', 'year'], right_on=['product_id', 'first_year'], how='inner')
    return res[['product_id', 'first_year', 'quantity', 'price']]