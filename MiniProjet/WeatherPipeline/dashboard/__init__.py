
from .layout import create_layout

def create_dashboard_app():
    """
    Crée et configure l'application Dash.
    """
    from dash import Dash
    app = Dash(__name__)
    app.layout = create_layout()
    return app
