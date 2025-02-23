import pandas as pd
import matplotlib.pyplot as plt

def generar_histograma_temperatura(csv_file, output_file):
    """
    Genera un histograma de distribución de temperatura a partir del archivo CSV.

    Parámetros:
    - csv_file: Ruta del archivo CSV con los datos.
    - output_file: Ruta donde se guardará la imagen del histograma.
    """
    # Cargar los datos
    df = pd.read_csv(csv_file)

    # Convertir la columna de temperatura a valores numéricos
    df["Temperatura (°C)"] = pd.to_numeric(df["Temperatura (°C)"], errors="coerce")

    # Crear el histograma
    plt.figure(figsize=(10, 6))
    plt.hist(df["Temperatura (°C)"], bins=40, color="royalblue", edgecolor="black", alpha=0.7)

    # Configurar el gráfico
    plt.xlabel("Temperatura (°C)")
    plt.ylabel("Frecuencia")
    plt.title("Distribución de la Temperatura")
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Guardar la imagen
    plt.savefig(output_file, dpi=300)
    plt.show()

# Ejecutar la función si el script se ejecuta directamente
if __name__ == "__main__":
    generar_histograma_temperatura("clima_maipu_extracted.csv", "graficos/histograma_temperatura.png")
