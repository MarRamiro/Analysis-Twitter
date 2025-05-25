# Importamos las bibliotecas necesarias
import pandas as pd
from googleapiclient.discovery import build
import time
from googleapiclient.errors import HttpError
import os

# Función con reintentos en caso de error 429 (límite de solicitudes alcanzado)
def analyze_toxicity_with_retry(text, retries=3, wait_time=60):
    for attempt in range(retries):
        try:
            return analyze_toxicity(text)  # Llama a la función que hace la solicitud
        except HttpError as e:
            if e.resp.status == 429:  # Verificamos si el error es por límite de cuota
                print(f"Cuota excedida. Esperando {wait_time} segundos antes de reintentar...")
                time.sleep(wait_time)  # Espera antes de reintentar
            else:
                raise e  # Si no es un error de límite de cuota, lo volvemos a lanzar
    print("Se ha alcanzado el número máximo de reintentos.")
    return None  # Devuelve None si no se pudo obtener el resultado después de los reintentos

# Cargar el archivo CSV desde una línea específica
start_line = 0  # Cambia esto a la línea desde la cual quieras empezar a procesar
file_path = 'nombre.csv'  # Ruta correcta del archivo CSV
df = pd.read_csv(file_path, skiprows=range(1, start_line))  # Omite las primeras 'start_line-1' filas

# Establecemos la clave de API de Google
API_KEY = "XXXXX"  # Asegúrate de reemplazar esto por tu clave API real 

# Construir el cliente de la API utilizando la clave de API
client = build(
    "commentanalyzer",  # El nombre del servicio
    "v1alpha1",  # La versión de la API
    developerKey=API_KEY,  # La clave de la API para autenticar la solicitud
    static_discovery=False  # Usamos discovery dinámico porque es más flexible y actual
)

# Crear una función para analizar la toxicidad de cada tuit
def analyze_toxicity(text):
    # Realizamos la solicitud a la Perspective API
    request = {
        'comment': {'text': text},
        'languages': ['es'],  # Especificamos que los comentarios están en español
        'requestedAttributes': {
            'TOXICITY': {},
            'SEVERE_TOXICITY': {},
            'IDENTITY_ATTACK': {},
            'INSULT': {},
            'PROFANITY': {},
            'THREAT': {}
        }  # Solicitamos la evaluación de todos los atributos
    }
    
    # Ejecutamos el análisis
    response = client.comments().analyze(body=request).execute()
    
    # Extraemos los valores de toxicidad de la respuesta
    attribute_scores = {
        'toxicity': response['attributeScores']['TOXICITY']['summaryScore']['value'],
        'severe_toxicity': response['attributeScores']['SEVERE_TOXICITY']['summaryScore']['value'],
        'identity_attack': response['attributeScores']['IDENTITY_ATTACK']['summaryScore']['value'],
        'insult': response['attributeScores']['INSULT']['summaryScore']['value'],
        'profanity': response['attributeScores']['PROFANITY']['summaryScore']['value'],
        'threat': response['attributeScores']['THREAT']['summaryScore']['value']
    }
    
    return attribute_scores

# Inicializamos las columnas de toxicidad en el DataFrame
toxicity_columns = ['toxicity', 'severe_toxicity', 'identity_attack', 'insult', 'profanity', 'threat']
for column in toxicity_columns:
    if column not in df.columns:
        df[column] = None  # Inicializamos las columnas con valores nulos

# Verificar si el archivo de salida ya existe
file_exists = os.path.exists('nombre.csv')

# Procesamos cada tuit y guardamos los resultados en el archivo CSV
for index, row in df.iterrows():
    if index % 100 == 0 or index == 0:
        print(f"Procesando tuit {index + 1}/{len(df)}...")  # Mensaje de depuración
    # Obtener los resultados de toxicidad para el tweet
    attribute_scores = analyze_toxicity_with_retry(row['texto_analisis'])
    
    if attribute_scores:  # Si se obtuvo una respuesta válida
        for key, value in attribute_scores.items():
            df.at[index, key] = value
    
    # Guardar el resultado inmediatamente en el archivo de salida
    row_df = df.iloc[[index]]
    
    # Si el archivo no existe, escribimos el encabezado, sino solo los datos
    row_df.to_csv('nombre.csv', mode='a', header=not file_exists, index=False)
    
    # Marcar que el archivo ahora existe para futuras iteraciones
    file_exists = True
    
    #time.sleep(0.1)  # Pausa de 1 segundo entre solicitudes
