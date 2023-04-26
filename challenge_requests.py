import requests
from datetime import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)

# Descargar la tabla de valores de la Unidad de Fomento actualizados desde la página web del SII
url = "https://www.sii.cl/valores_y_fechas/uf/uf{}.htm".format(datetime.now().year)
response = requests.get(url)
data = response.content.decode("utf-8")

# Leer los datos de la tabla y guardarlos en un diccionario
uf_data = {}
for line in data.split("\n"):
    if "<tr" in line:
        columns = line.split("</td><td>")
        # import ipdb
        print("line:", line)
        print(columns)
        # ipdb.set_trace()
        if len(columns) > 2:
            date_str = columns[0].replace("<tr><td>", "")
            value_str = (
                columns[1].replace("</td></tr>", "").replace(".", "").replace(",", ".")
            )
            date = datetime.strptime(date_str, "%d-%m-%Y")
            uf_data[date] = float(value_str)


# Crear la API para consultar la UF
@app.route("/uf/<fecha>", methods=["GET"])
def get_uf(fecha):
    # Validar que la fecha ingresada esté en el rango permitido
    date_str = fecha

    try:
        date = datetime.strptime(date_str, "%d-%m-%Y")
        if date < datetime(2013, 1, 1) or date > datetime.now():
            raise ValueError
    except:
        return jsonify({"error": "Fecha inválida"}), 400

    # Buscar el valor de la UF correspondiente a la fecha ingresada
    value = uf_data.get(date)

    # Devolver el valor de la UF en formato JSON
    if value:
        return jsonify({"valor": value})
    else:
        return jsonify({"error": "Valor de UF no encontrado"}), 404


if __name__ == "__main__":
    app.run()
