import pandas as pd
import matplotlib.pyplot as plt

def graficar_humedad(csv_file, output_file="graficos/humedad_diaria.png"):
    """Genera un gráfico de humedad a lo largo del día para cada año."""
    
    # Cargar los datos
    df = pd.read_csv(csv_file)

    # Convertir la columna de hora en tipo datetime para facilitar el orden
    df["Hora"] = pd.to_datetime(df["Hora"], format="%H:%M").dt.hour

    # Configurar el gráfico
    plt.figure(figsize=(10, 5))

    # Obtener los años únicos
    años = df["Año"].unique()

    # Graficar la humedad para cada año
    for año in años:
        datos_año = df[df["Año"] == año]
        plt.plot(datos_año["Hora"], datos_año["Humedad (%)"], marker="o", label=f"{año}")

    # Configuraciones del gráfico
    plt.xlabel("Hora del Día")
    plt.ylabel("Humedad (%)")
    plt.title("Variación de Humedad a lo largo del Día")
    plt.xticks(range(0, 24))
    plt.legend()
    plt.grid(True)

    # Guardar y mostrar el gráfico
    plt.savefig(output_file)
    plt.show()

# Prueba el script llamando la función
if __name__ == "__main__":
    graficar_humedad("clima_maipu_extracted.csv")
