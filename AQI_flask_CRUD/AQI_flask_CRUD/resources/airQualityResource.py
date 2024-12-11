from flask_restful import Resource
from flask import request
import json

air_quality_data = [
    {
        "id": 1,
        "City": "Delhi",
        "Date": "2024-01-01",
        "PM2.5": 150,
        "PM10": 300,
        "NO": 50,
        "NO2": 80,
        "NOx": 100,
        "NH3": 20,
        "CO": 1.2,
        "SO2": 5,
        "O3": 70,
        "Benzene": 2.0,
        "Toluene": 5.1,
        "Xylene": 0.5,
        "AQI": 250,
        "AQI_Bucket": "Poor"
    }
]

class AirQualityGETResource(Resource):
    def get(self):
        return air_quality_data

class AirQualityEntryGETResource(Resource):
    def get(self, id):
        for entry in air_quality_data:
            if entry["id"] == id:
                return entry
        return None, 404

class AirQualityPOSTResource(Resource):
    def post(self):
        entry = json.loads(request.data)
        new_id = max(item["id"] for item in air_quality_data) + 1 if air_quality_data else 1
        entry["id"] = new_id
        air_quality_data.append(entry)
        return entry, 201

class AirQualityPUTResource(Resource):
    def put(self, id):
        updated_entry = json.loads(request.data)
        for entry in air_quality_data:
            if entry["id"] == id:
                entry.update(updated_entry)
                return entry, 200
        return None, 404

class AirQualityDELETEResource(Resource):
    def delete(self, id):
        global air_quality_data
        air_quality_data = [entry for entry in air_quality_data if entry["id"] != id]
        return "", 204
