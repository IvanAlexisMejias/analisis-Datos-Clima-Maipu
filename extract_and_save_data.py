import json
import pandas as pd

def load_json(file_path):
    """Carga el archivo JSON."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def extract_data(json_data):
    """Extrae los datos del JSON y los transforma en un DataFrame de pandas."""
    records = []
    for year, data in json_data.items():
        for hour, values in data["horas"].items():
            record = {
                "Año": int(year),
                "Fecha": data["fecha"],
                "Ubicación": data["ubicacion"],
                "Hora": hour,
                "Temperatura (°C)": values.get("temperatura", None),
                "Clima": values.get("clima", None),
                "Precipitaciones (mm)": values.get("precipitaciones", None),
                "Probabilidad de Nevada": values.get("probabilidad_nevada", None),
                "Humedad (%)": values.get("humedad", None),
                "Velocidad del Viento (km/h)": values.get("velocidad_viento", None),
                "Ráfaga de Viento (km/h)": values.get("rafaga_viento", None),
                "Ángulo del Viento (°)": values.get("angulo_viento", None),
                "Dirección del Viento": values.get("direccion_viento", None),
                "Nubosidad": values.get("nubosidad", None),
                "Visibilidad (km)": values.get("visibilidad", None)
            }
            records.append(record)
    return pd.DataFrame(records)

def save_to_csv(df, output_file):
    """Guarda el DataFrame en un archivo CSV."""
    df.to_csv(output_file, index=False, encoding='utf-8')

def save_to_excel(df, output_file):
    """Guarda el DataFrame en un archivo Excel."""
    df.to_excel(output_file, index=False, engine='openpyxl')

def main():
    """Ejecuta la extracción y guardado de datos."""
    input_file = "clima_maipu.json"  # Archivo JSON en la misma carpeta
    csv_output = "clima_maipu_extracted.csv"
    excel_output = "clima_maipu.xlsx"
    
    json_data = load_json(input_file)
    df = extract_data(json_data)
    save_to_csv(df, csv_output)
    save_to_excel(df, excel_output)
    
    print(f"✅ Datos extraídos y guardados en {csv_output} y {excel_output}")

if __name__ == "__main__":
    main()
