from datetime import datetime
from flask import Flask, Response, jsonify
from typing import Tuple
from request_to_csv import fetch_dataframe_from_api


class UFService:
    def __init__(self, date: datetime):
        self.date = date

    def get_uf(self) -> Tuple:
        try:
            if self.date.year > 2013 or self.date.year <= datetime.datetime.now().year:
                df = fetch_dataframe_from_api(self.date)

        except:
            return jsonify({"error": "Fecha inválida"}), 400

        if not df.empty:
            return Response(
                df.to_json(force_ascii=False).encode("utf-8"),
                mimetype="application/json",
            )

        else:
            return jsonify({"error": "Valor de UF no encontrado"}), 404


app = Flask(__name__)


@app.route("/uf/<date>", methods=["GET"])
def get_uf(date):
    parsed_date = datetime.strptime(f"{date}-01-01", "%Y-%m-%d")
    uf_service = UFService(parsed_date)
    return uf_service.get_uf()


if __name__ == "__main__":
    app.run()
