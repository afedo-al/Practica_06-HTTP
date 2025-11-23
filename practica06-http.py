from flask import Flask, request, jsonify
from datetime import datetime

app = Flask("practica6_app")

lista_sensores = []

def hora_iso():
    return datetime.now().isoformat()

def validar_json_sensor(info):
    faltantes = []
    for campo in ["sensor_id", "name", "value"]:
        if campo not in info:
            faltantes.append(campo)

    if faltantes:
        return {"error": f"Faltan campos: {', '.join(faltantes)}"}

    if type(info["sensor_id"]) != str or info["sensor_id"] == "":
        return {"error": "sensor_id debe ser texto"}

    if type(info["name"]) != str or info["name"] == "":
        return {"error": "name debe ser texto"}

    if type(info["value"]) not in [int, float]:
        return {"error": "value debe ser numérico"}

    if info["value"] < -1000 or info["value"] > 1000:
        return {"error": "value fuera de rango permitido"}

    return None


@app.route("/api/sensors", methods=["POST"])
def crear_sensor():
    if not request.is_json:
        return jsonify({"error": "El cuerpo debe ser JSON"}), 400

    datos = request.get_json()

    if type(datos) != dict:
        return jsonify({"error": "Formato JSON inválido"}), 400

    error = validar_json_sensor(datos)
    if error:
        return jsonify(error), 400

    for s in lista_sensores:
        if s["sensor_id"] == datos["sensor_id"]:
            return jsonify({"error": "sensor_id ya existe"}), 400

    nuevo = {
        "sensor_id": datos["sensor_id"],
        "name": datos["name"],
        "value": datos["value"],
        "unit": datos.get("unit", ""),
        "location": datos.get("location", ""),
        "created_at": hora_iso(),
        "updated_at": hora_iso()
    }

    lista_sensores.append(nuevo)

    return jsonify({
        "mensaje": "Sensor creado correctamente",
        "sensor": nuevo
    }), 201


@app.route("/api/sensors/<sensor_id>", methods=["DELETE"])
def eliminar_sensor(sensor_id):
    encontrado = None

    for s in lista_sensores:
        if s["sensor_id"] == sensor_id:
            encontrado = s
            break

    if encontrado is None:
        return jsonify({"error": "Sensor no encontrado"}), 404

    lista_sensores.remove(encontrado)

    return jsonify({
        "mensaje": "Sensor eliminado",
        "id_eliminado": sensor_id,
        "timestamp": hora_iso()
    }), 200


@app.route("/api/sensors", methods=["GET"])
def listar():
    return jsonify({"cantidad": len(lista_sensores), "sensores": lista_sensores})


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, True)
