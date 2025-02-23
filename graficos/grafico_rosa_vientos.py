import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def generar_rosa_vientos(csv_file, output_file):
    """
    Genera una Rosa de los Vientos basada en la dirección y velocidad del viento.

    Parámetros:
    - csv_file: Ruta del archivo CSV con los datos.
    - output_file: Ruta donde se guardará la imagen de la Rosa de los Vientos.
    """
    # Cargar los datos
    df = pd.read_csv(csv_file)

    # Convertir los valores a numéricos
    df["Ángulo del Viento (°)"] = pd.to_numeric(df["Ángulo del Viento (°)"], errors="coerce")
    df["Velocidad del Viento (km/h)"] = pd.to_numeric(df["Velocidad del Viento (km/h)"], errors="coerce")

    # Convertir ángulos a radianes
    angles = np.radians(df["Ángulo del Viento (°)"])
    speeds = df["Velocidad del Viento (km/h)"]

    # Crear la figura en forma polar
    plt.figure(figsize=(8, 8))
    ax = plt.subplot(111, polar=True)

    # Crear histograma en coordenadas polares
    bins = np.linspace(0, 2*np.pi, 36)  # 36 bins (cada 10 grados)
    ax.hist(angles, bins=bins, weights=speeds, color="skyblue", edgecolor="black", alpha=0.7)

    # Configurar la rosa de los vientos
    ax.set_theta_zero_location("N")  # Norte en la parte superior
    ax.set_theta_direction(-1)  # Dirección en sentido horario
    ax.set_xticks(np.radians([0, 45, 90, 135, 180, 225, 270, 315]))
    ax.set_xticklabels(["N", "NE", "E", "SE", "S", "SO", "O", "NO"])

    ax.set_title("Rosa de los Vientos", fontsize=14)

    # Guardar la imagen
    plt.savefig(output_file, dpi=300)
    plt.show()

# Ejecutar si el script se corre directamente
if __name__ == "__main__":
    generar_rosa_vientos("clima_maipu_extracted.csv", "graficos/rosa_vientos.png")
