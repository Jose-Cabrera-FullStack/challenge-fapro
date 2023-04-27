from datetime import datetime
from request_to_csv import fetch_dataframe_from_api


def test_fetch_data_from_api():
    date = datetime.strptime("2019-01-01", "%Y-%m-%d")
    df = fetch_dataframe_from_api(date)
    month_list = [
        "Ene",
        "Feb",
        "Mar",
        "Abr",
        "May",
        "Jun",
        "Jul",
        "Ago",
        "Sep",
        "Oct",
    ]

    assert not df.empty
    assert all(month in df.columns for month in month_list)
