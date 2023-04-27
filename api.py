from datetime import datetime
from flask import Flask, Response, jsonify
from typing import List, Tuple
from request_to_csv import fetch_dataframe_from_api


class UFService:
    def __init__(self, api: fetch_dataframe_from_api):
        self.api = api


def get_uf(self, date: str) -> Tuple:
    parsed_date = datetime.strptime(f"{date}-01-01", "%Y-%m-%d")
    try:
        if parsed_date.year > 2013 or parsed_date.year <= datetime.datetime.now().year:
            df = self.api.fetch_dataframe_from_api(parsed_date)

    except:
        return jsonify({"error": "Fecha inválida"}), 400

    if not df.empty:
        return Response(
            df.to_json(force_ascii=False).encode("utf-8"), mimetype="application/json"
        )

    else:
        return jsonify({"error": "Valor de UF no encontrado"}), 404


app = Flask(__name__)
uf_service = UFService(fetch_dataframe_from_api)


@app.route("/uf/<date>", methods=["GET"])
def get_uf(date):
    return uf_service.get_uf(date)


if __name__ == "__main__":
    app.run()
