import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generar_mapa_calor(archivo_csv):
    """Genera un mapa de calor de temperatura a lo largo del día para diferentes años."""
    # Cargar datos
    df = pd.read_csv(archivo_csv)

    # Convertir la hora en formato numérico para ordenarlo correctamente
    df['Hora'] = df['Hora'].str[:2].astype(int)

    # Crear una tabla pivote con los años como filas y las horas como columnas
    heatmap_data = df.pivot_table(index="Año", columns="Hora", values="Temperatura (°C)", aggfunc="mean")

    # Configurar la figura
    plt.figure(figsize=(12, 6))
    sns.heatmap(heatmap_data, cmap="coolwarm", annot=True, fmt=".1f", linewidths=0.5)

    # Etiquetas y título
    plt.title("Mapa de Calor de Temperatura a lo Largo del Día", fontsize=14)
    plt.xlabel("Hora del Día", fontsize=12)
    plt.ylabel("Año", fontsize=12)
    plt.xticks(rotation=0)
    
    # Guardar imagen
    plt.savefig("graficos/mapa_calor_temperatura.png", dpi=300, bbox_inches="tight")
    plt.show()

# Si quieres probarlo directamente
if __name__ == "__main__":
    generar_mapa_calor("clima_maipu_extracted.csv")
