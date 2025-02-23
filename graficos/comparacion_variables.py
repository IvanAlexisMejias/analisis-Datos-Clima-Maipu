import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generar_grafico_comparacion(csv_file, var_x, var_y):
    """Genera un gráfico de dispersión para comparar dos variables climáticas."""
    # Cargar los datos
    df = pd.read_csv(csv_file)

    # Configuración del gráfico
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=var_x, y=var_y, hue="Año", palette="coolwarm", edgecolor="black", alpha=0.7)

    # Títulos y etiquetas
    plt.title(f"Comparación entre {var_x} y {var_y}")
    plt.xlabel(var_x)
    plt.ylabel(var_y)
    plt.legend(title="Año")
    plt.grid(True, linestyle="--", alpha=0.6)

    # Guardar la imagen
    plt.tight_layout()
    filename = f"graficos/comparacion_{var_x}_{var_y}.png"
    plt.savefig(filename)
    plt.show()

# Prueba con diferentes variables
if __name__ == "__main__":
    csv_file = "clima_maipu_extracted.csv"
    
    # Comparación 1: Temperatura vs Humedad
    generar_grafico_comparacion(csv_file, "Temperatura (°C)", "Humedad (%)")
    
    # Comparación 2: Velocidad del Viento vs Nubosidad
    generar_grafico_comparacion(csv_file, "Velocidad del Viento (km/h)", "Nubosidad")

    # Comparación 3: Temperatura vs Velocidad del Viento
    generar_grafico_comparacion(csv_file, "Temperatura (°C)", "Velocidad del Viento (km/h)")
