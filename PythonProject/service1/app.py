from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from service1"}

@app.get("/call_service2")
def call_service2():
    # Вызовем эндпоинт второго сервиса
    response = requests.get("http://service2:8001/data")
    return {"service2_response": response.json()}
