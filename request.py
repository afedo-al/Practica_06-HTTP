import requests
import json

BASE_URL = "http://127.0.0.1:5000/api/sensors"

def crear_sensor():
    sensor = {
        "sensor_id": "01",
        "name": "temperatura",
        "value": 23.5,
        "unit": "C",
        "location": "laboratorio"
    }

    respuesta = requests.post(BASE_URL, json=sensor)

    print("\n POST /api/sensors ===")
    print("Código:", respuesta.status_code)
    print(json.dumps(respuesta.json(), indent=4))


def listar_sensores():
    respuesta = requests.get(BASE_URL)

    print("\n GET /api/sensors ===")
    print("Código:", respuesta.status_code)
    print(json.dumps(respuesta.json(), indent=4))


def borrar_sensor(sensor_id):
    url = f"{BASE_URL}/{sensor_id}"
    respuesta = requests.delete(url)

    print(f"\n DELETE /api/sensors/{sensor_id} ===")
    print("Código:", respuesta.status_code)
    print(json.dumps(respuesta.json(), indent=4))


if __name__ == "__main__":
    print("\n ENVIANDO SENSOR ")
    crear_sensor()

    print("\n LISTANDO SENSORES ")
    listar_sensores()

    print("\n BORRANDO SENSOR ")
    borrar_sensor("01")

    print("\n LISTANDO NUEVAMENTE ")
    listar_sensores()
