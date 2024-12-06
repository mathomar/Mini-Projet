from dash import dcc, html
import plotly.express as px
import pandas as pd
from pymongo import MongoClient

def fetch_data_from_mongodb():
    """
    Récupérer les données météo depuis MongoDB.
    :return: Liste de dictionnaires avec les données.
    """
    client = MongoClient("mongodb://localhost:27017/")  # Connexion locale
    db = client.weatherDB  # Nom de la base de données
    collection = db.weatherData  # Nom de la collection

    # Récupération des données
    data = list(collection.find({}, {"_id": 0}))  # Exclure le champ _id
    return data

def create_layout():
    """
    Créer la mise en page du tableau de bord avec les données MongoDB.
    """
    # Récupérer les données depuis MongoDB
    data = fetch_data_from_mongodb()

    # Créer un DataFrame pour Plotly
    df = pd.DataFrame(data)

    # Créer un graphique interactif
    fig = px.bar(df, x="city", y="temperature", title="Temperature per City")

    # Retourner la mise en page
    return html.Div([
        dcc.Graph(id="bar-chart", figure=fig)
    ])
