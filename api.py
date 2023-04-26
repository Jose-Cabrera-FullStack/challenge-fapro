import pandas as pd
from flask import Flask, Response, jsonify
from datetime import datetime

from request_to_csv import fetch_data_from_api

app = Flask(__name__)


# Crear la API para consultar la UF
@app.route("/uf/<date>", methods=["GET"])
def get_uf(date):
    parsed_date = datetime.strptime(f"{date}-01-01", "%Y-%m-%d")
    try:
        # validate date in this try except
        if parsed_date.year > 2013 or parsed_date.year <= datetime.datetime.now().year:
            df = fetch_data_from_api(parsed_date)

    except:
        return jsonify({"error": "Fecha inválida"}), 400

    if not df.empty:
        # import ipdb

        # ipdb.set_trace()
        # # return df.to_json(force_ascii=False).encode("utf-8")
        return Response(
            df.to_json(force_ascii=False).encode("utf-8"), mimetype="application/json"
        )

    else:
        return jsonify({"error": "Valor de UF no encontrado"}), 404


if __name__ == "__main__":
    app.run()
