from dash import Dash
from dashboard import create_dashboard_app

app = create_dashboard_app()

if __name__ == "__main__":
    app.run_server(debug=True)

    