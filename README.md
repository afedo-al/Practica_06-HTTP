# Práctica 6 – Implementación del Protocolo HTTP

## API REST para Gestión de Sensores

### 👥 Integrantes del Equipo

- **Moises A Sunza Vazquez**
- **Wilbert J Novelo Ruiz**
- **Kevin J Ruiz Tillit**
- **Alfredo J Cruz Miss**
- **Ulises Zarate Concha**

_(Edita esta sección con los nombres reales de tu equipo)_

---

## 📘 Descripción

Esta práctica implementa un servidor HTTP utilizando **Flask** en Raspberry Pi Zero.  
El sistema permite crear y eliminar sensores mediante los métodos HTTP:

- **POST** → Crear sensores
- **DELETE** → Eliminar sensores
- **GET** (opcional) → Consultar sensores registrados

Los sensores cuentan con:

- `sensor_id`
- `name`
- `value`
- `unit`
- `location`
- `created_at`
- `updated_at`

---

## 📡 Endpoints Implementados

### ➤ **POST /api/sensors**

Crea un nuevo sensor.

#### **JSON requerido:**

```json
{
  "sensor_id": "01",
  "name": "temperatura",
  "value": 22.5,
  "unit": "celsius",
  "location": "lab1"
}
```
