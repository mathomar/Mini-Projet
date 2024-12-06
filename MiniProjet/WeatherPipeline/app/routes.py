from flask import Blueprint, request, jsonify
from .models import get_weather, save_to_mongodb

from .models import is_extreme_weather, send_notification


routes = Blueprint('routes', __name__)

@routes.route('/weather', methods=['GET'])
def fetch_weather():
    """
    Route pour récupérer les données météo via l'API et les sauvegarder.
    """
    city = request.args.get('city', 'Paris')
    data = get_weather(city)
    return jsonify(data)

@routes.route('/get_weather', methods=['GET'])
def get_weather_data():
    """
    Route pour récupérer toutes les données sauvegardées dans MongoDB.
    """
    try:
        data = get_all_weather()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@routes.route('/check_weather', methods=['POST'])


def check_weather():
    """
    Route pour vérifier les conditions météo et envoyer une notification si nécessaire.
    """
    data = request.json  # Les données météo sont envoyées en JSON dans la requête
    if not data:
        return jsonify({"error": "No data provided"}), 400

    try:
        # Vérifier si les conditions sont extrêmes
        if is_extreme_weather(data):
            # Envoyer une notification
            email = "omarcr2894@gmail.com"
            subject = "Alerte météo : Conditions extrêmes détectées"
            message = f"Attention ! Les conditions météorologiques suivantes ont été détectées :\n{data}"
            send_notification(email, subject, message)
            return jsonify({"message": "Notification envoyée"}), 200
        else:
            return jsonify({"message": "Pas de conditions extrêmes détectées"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
