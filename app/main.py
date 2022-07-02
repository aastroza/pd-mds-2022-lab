import joblib
import numpy as np
import io
import uvicorn
import nest_asyncio
from enum import Enum
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

rfc = joblib.load("./model/random_forest.joblib")

def predict_taxi_trip(features_trip, confidence=0.5):
    """Recibe un vector de características de un viaje en taxi en NYC y predice 
       si el pasajero dejará o no una propina alta.

    Argumentos:
        features_trip (array): Características del viaje, vector de tamaño 11.
        confidence (float, opcional): Nivel de confianza. Por defecto es 0.5.
    """
    
    pred_value = rfc.predict_proba(features_trip.reshape(1, -1))[0][1]
    if pred_value >= confidence:
      return 1
    else:
      return 0

# Asignamos una instancia de la clase FastAPI a la variable "app".
# Interacturaremos con la API usando este elemento.
app = FastAPI(title='Implementando un modelo de Machine Learning usando FastAPI')

# Creamos una clase para el vector de features de entrada
class Item(BaseModel):
    pickup_weekday: float
    pickup_hour: float
    work_hours: float
    pickup_minute: float
    passenger_count: float
    trip_distance: float
    trip_time: float
    trip_speed: float
    PULocationID: float
    DOLocationID: float
    RatecodeID: float

# Usando @app.get("/") definimos un método GET para el endpoint / (que sería como el "home").
@app.get("/")
def home():
    return "¡Felicitaciones! Tu API está funcionando según lo esperado. Anda ahora a http://localhost:8000/docs."


# Este endpoint maneja la lógica necesaria para clasificar.
# Requiere como entrada el vector de características del viaje y el umbral de confianza para la clasificación.
@app.post("/predict") 
def prediction(item: Item, confidence: float):

    
    # 1. Correr el modelo de clasificación
    features_trip = np.array([item.pickup_weekday, item.pickup_hour, item.work_hours, item.pickup_minute, item.passenger_count, item.trip_distance,
                    item.trip_time, item.trip_speed, item.PULocationID, item.DOLocationID, item.RatecodeID])
    pred = predict_taxi_trip(features_trip, confidence)
    
    # 2. Transmitir la respuesta de vuelta al cliente

    # Retornar el resultado de la predicción
    return {'predicted_class': pred}

