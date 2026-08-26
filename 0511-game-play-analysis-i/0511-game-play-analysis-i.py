import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    res= activity.sort_values('event_date')
    res= (res.drop_duplicates('player_id')[['player_id','event_date']].rename(columns={'event_date': 'first_login'}))
    return res