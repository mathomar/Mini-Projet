import requests
from pymongo import MongoClient

# Configuration MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Connexion locale
db = client.weatherDB  # Nom de la base de données
collection = db.weatherData  # Nom de la collection

# Configuration de l'API OpenWeather
API_KEY = "d7c70474a0035e137cd734204ac78244"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """
    Récupérer les données météo pour une ville.
    :param city: Nom de la ville.
    :return: Données JSON ou message d'erreur.
    """
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        save_to_mongodb(data)
        return data
    else:
        return {"error": f"Failed to fetch data for {city}"}

def save_to_mongodb(data):
    """
    Sauvegarder les données météo dans MongoDB.
    :param data: Données JSON de l'API.
    """
    document = {
        "city": data.get("name"),
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["description"]
    }
    result = collection.insert_one(document)
    print(f"Data inserted with ID: {result.inserted_id}")
