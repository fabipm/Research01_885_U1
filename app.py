import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Crear una aplicación Dash
app = dash.Dash(__name__)

# Datos de ejemplo
data = {
    "Fecha": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05"],
    "Ventas": [100, 400, 300, 500, 450],
    "Categoría": ["Electrónica", "Electrónica", "Ropa", "Ropa", "Electrónica"]
}
df = pd.DataFrame(data)
df["Fecha"] = pd.to_datetime(df["Fecha"])

# Crear un gráfico interactivo
fig = px.line(df, x="Fecha", y="Ventas", color="Categoría", title="Ventas por Categoría")

# Layout de la aplicación
app.layout = html.Div([
    html.H1("Dashboard de Ventas"),
    dcc.Graph(figure=fig)
])

# --- Agregar esto para que Gunicorn pueda usar el servidor ---
server = app.server

# Para correr localmente
if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8080, debug=True)
