import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
df = pd.read_csv("clima_maipu_extracted.csv")

# Seleccionar las variables a graficar
variables = ["Temperatura (°C)", "Humedad (%)", "Velocidad del Viento (km/h)"]

# Crear el boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(data=df[variables])

# Configuración del gráfico
plt.title("Boxplot de Temperatura, Humedad y Velocidad del Viento")
plt.ylabel("Valor")
plt.xticks(range(len(variables)), variables)

# Guardar el gráfico
plt.savefig("graficos/boxplot_variables.png")
plt.show()
