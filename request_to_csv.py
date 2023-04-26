import requests

import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime


def fetch_data_from_api(date):
    year = datetime.strptime(date.strftime("%Y-%m-%d"), "%Y-%m-%d").year

    url = "https://www.sii.cl/valores_y_fechas/uf/uf{}.htm".format(year)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extraer los datos de la tabla
    table = soup.find(id="table_export")

    fomento_df = pd.read_html(str(table))[0]

    fomento_df = fomento_df.drop(columns=["Día"])

    return fomento_df
