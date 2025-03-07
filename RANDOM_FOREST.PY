import pandas as pd
import py7zr
import os


def extraer_y_cargar(archivo_7z, nombre_archivo, formato="csv"):
    with py7zr.SevenZipFile(archivo_7z, mode="r") as z:
        z.extractall(path="temp")  # Extraer en una carpeta temporal

    ruta_extraida = os.path.join("temp", nombre_archivo)

    if formato == "csv":
        df = pd.read_csv(ruta_extraida)
    elif formato == "excel":
        df = pd.read_excel(ruta_extraida)
    else:
        raise ValueError("Formato no soportado")

    return df


# Ejemplo de uso
try:
    df = extraer_y_cargar("all_faults_dataset.7z", "all_faults_dataset.csv")
except ValueError as e:
    print(e)
print(df.head())  # Mostrar las primeras filas
print(df.columns)
