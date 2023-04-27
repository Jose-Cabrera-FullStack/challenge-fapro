import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from typing import List


def get_url(date: datetime) -> str:
    year = date.year
    return f"https://www.sii.cl/valores_y_fechas/uf/uf{year}.htm"


def get_html(url: str) -> str:
    response = requests.get(url)
    return response.content


def parse_table(html: str) -> pd.DataFrame:
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find(id="table_export")
    dataframe = pd.read_html(str(table))[0]
    return dataframe


def remove_day_column(dataframe: pd.DataFrame) -> pd.DataFrame:
    dataframe = dataframe.drop(columns=["Día"])
    return dataframe


def fetch_dataframe_from_api(date: datetime) -> List[List[str]]:
    url = get_url(date)
    html = get_html(url)
    dataframe = parse_table(html)
    dataframe = remove_day_column(dataframe)
    return dataframe


# import requests

# import pandas as pd
# from bs4 import BeautifulSoup
# from datetime import datetime


# def fetch_data_from_api(date):
#     year = datetime.strptime(date.strftime("%Y-%m-%d"), "%Y-%m-%d").year

#     url = "https://www.sii.cl/valores_y_fechas/uf/uf{}.htm".format(year)
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, "html.parser")

#     table = soup.find(id="table_export")

#     fomento_df = pd.read_html(str(table))[0]

#     fomento_df = fomento_df.drop(columns=["Día"])

#     return fomento_df
