from flask_restful import Resource
from flask import request
import json


air_quality_data = [
    {
        "id": 1,
        "City": "Delhi",
        "Date": "2018-02-23",
        "PM2.5": 163.75,
        "PM10": 333.99,
        "NO": 59.63,
        "NO2": 70.77,
        "NOx": 92.54,
        "NH3": 59.64,
        "CO": 1.81,
        "SO2": 16.26,
        "O3": 48.62,
        "Benzene": 3.89,
        "Toluene": 9.53,
        "Xylene": 0.0,
        "AQI": 331.0,
        "AQI_Bucket": "Very Poor"
    },
    {
        "id": 2,
        "City": "Gurugram",
        "Date": "2020-05-05",
        "PM2.5": 55.54,
        "PM10": 94.42,
        "NO": 4.16,
        "NO2": 13.71,
        "NOx": 10.97,
        "NH3": 16.73,
        "CO": 0.81,
        "SO2": 7.78,
        "O3": 67.79,
        "Benzene": 5.46,
        "Toluene": 3.24,
        "Xylene": 2.49,
        "AQI": 130.0,
        "AQI_Bucket": "Moderate"
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
