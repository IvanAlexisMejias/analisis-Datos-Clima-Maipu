import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D


def generar_animacion_3D(csv_file, output_gif):
    """
    Genera un GIF animado mostrando la evolución de la temperatura en un gráfico 3D.

    Parámetros:
    - csv_file: Ruta del archivo CSV con los datos.
    - output_gif: Ruta donde se guardará el GIF animado.
    """
    # Cargar los datos
    df = pd.read_csv(csv_file)

    # Asegurarse de que 'Hora' sea numérico
    df['Hora'] = pd.to_numeric(df['Hora'], errors='coerce')

    # Crear la figura 3D
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    # Configurar ejes
    ax.set_xlim(0, 23)  # Horas de 00:00 a 23:00
    ax.set_ylim(df['Año'].min(), df['Año'].max())
    ax.set_zlim(df["Temperatura (°C)"].min() - 2, df["Temperatura (°C)"].max() + 2)
    ax.set_xlabel("Hora del Día")
    ax.set_ylabel("Año")
    ax.set_zlabel("Temperatura (°C)")
    ax.set_title("Evolución 3D de la Temperatura")

    # Crear el scatter plot inicial
    scatter = ax.scatter([], [], [], c=[], cmap='coolwarm', s=50)

    # Función de inicialización
    def init():
        scatter._offsets3d = ([], [], [])
        return scatter,

    # Función de animación
    def animate(i):
        # Filtrar hasta el año actual
        years = sorted(df["Año"].unique())
        current_year = years[i % len(years)]
        df_year = df[df['Año'] == current_year]

        x = df_year['Hora'].values
        y = df_year['Año'].values
        z = df_year['Temperatura (°C)'].values
        colors = z  # Colorear por temperatura

        scatter._offsets3d = (x, y, z)
        scatter.set_array(colors)

        ax.set_title(f"Evolución 3D de la Temperatura - Año {current_year}")
        ax.view_init(elev=30, azim=i * 4)  # Rotar la vista para efecto dinámico
        return scatter,

    # Crear la animación
    ani = animation.FuncAnimation(fig, animate, init_func=init,
                                  frames=len(df["Año"].unique()) * 10,
                                  interval=200, blit=False)

    # Guardar la animación como GIF
    ani.save(output_gif, writer='pillow', fps=10)
    print(f"✅ GIF guardado en: {output_gif}")


# Ejecutar si el script se corre directamente
if __name__ == "__main__":
    generar_animacion_3D("clima_maipu_extracted.csv", "graficos/animacion_temperatura_3D.gif")
