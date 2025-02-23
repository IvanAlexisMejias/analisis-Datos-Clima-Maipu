import pandas as pd
import matplotlib.pyplot as plt

def generar_grafico_clima(csv_file):
    """Genera un gráfico de barras apiladas mostrando la frecuencia de los climas en cada hora del día."""
    # Cargar los datos
    df = pd.read_csv(csv_file)

    # Filtrar columnas necesarias
    df_clima = df.pivot_table(index="Hora", columns="Clima", aggfunc="size", fill_value=0)

    # Colores personalizados para cada clima
    colores = {
        "Despejado": "#FFD700",  # Amarillo
        "Soleado": "#FFA500",  # Naranja
        "Parcialmente nublado": "#87CEEB",  # Azul cielo
        "Nublado": "#708090",  # Gris
        "Lluvia": "#4682B4",  # Azul
        "Tormenta": "#800080"  # Morado
    }

    # Graficar barras apiladas
    df_clima.plot(kind="bar", stacked=True, color=[colores.get(c, "#CCCCCC") for c in df_clima.columns], figsize=(12, 6))

    plt.title("Distribución del Clima a lo Largo del Día")
    plt.xlabel("Hora del Día")
    plt.ylabel("Frecuencia")
    plt.xticks(rotation=45)
    plt.legend(title="Tipo de Clima", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Guardar el gráfico
    plt.tight_layout()
    plt.savefig("graficos/clima_diario.png")
    plt.show()

# Prueba del gráfico
if __name__ == "__main__":
    generar_grafico_clima("clima_maipu_extracted.csv")
