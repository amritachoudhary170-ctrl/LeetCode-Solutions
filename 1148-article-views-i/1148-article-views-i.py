import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    res = views[views["author_id"] == views["viewer_id"]]

    return pd.DataFrame({"id": sorted(res["author_id"].unique())})