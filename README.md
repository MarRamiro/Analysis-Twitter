# Hate Speech on Twitter: Analysis of LGBTIQ-phobia Before and After Elon Musk

This repository contains the code used for the implementation of the Bachelor's thesis (Trabajo de Fin de Grado) at the Faculty of Computer Science of the Complutense University of Madrid.

## Project Overview

The project, titled **"Hate Speech in Twitter: Analysis of LGTBIQ-phobia Before and After Elon Musk"**, is the first study in Spanish that analyzes the situation of LGTBIQ-phobia on Twitter following Musk’s acquisition of the platform. The study focuses on tweets in Spanish from June 28th of each year (Pride Day), ranging from 2015 to 2024. For this analysis, a dataset of 653,000 tweets related to the LGTBIQ+ community was collected. As a benchmark for comparison, a second dataset of 395,000 random tweets was collected.

## Dataset Collection

The datasets were obtained using [twitterapi.io](https://twitterapi.io/) and the code in the repository starting with `descarga_datos`. These datasets include:

- **LGTBIQ+ related tweets** (653,000)
- **Random tweets** (395,000)

These datasets can be found in the following link: [Zenodo poyect](https://zenodo.org/records/15639492)

## Toxicity Classification

The collected datasets were classified using the [Perspective API](https://perspectiveapi.com/) to analyze the level of toxicity. This classification process is handled by the code in the `analisis_toxicidad.py` file.

## Statistical Analysis

The statistical analysis of the data is conducted in the `analisis_estadistico.ipynb` file, which includes key metrics and comparisons.

## Graphs and Visualizations

Graphs and visualizations are generated in the `graficas.ipynb` and `graficas_trans.ipynb` files, with the latter specifically focusing on a sub-analysis related to transgender individuals.

---

### Files in this Repository:

1. **LICENSE**: Licensing information for the project.
2. **README.md**: This file, providing an overview of the repository.
3. **analisis_estadistico.ipynb**: Contains the statistical analysis of the datasets.
4. **analisis_toxicidad.py**: Script for toxicity classification using the Perspective API.
5. **descarga_datos_aleatorios.py**: Code for downloading random tweets.
6. **descarga_datos_colectivo.py**: Code for downloading LGTBIQ+ related tweets.
7. **graficas.ipynb**: Notebook for generating graphs and visualizations.
8. **graficas_trans.ipynb**: Notebook for visualizing data related to transgender individuals.
9. **thesis.pdf**: Contains the Bachelor's thesis, detailing the research and analysis conducted.

## Instructions to Replicate the Work

To replicate the work, please follow these instructions:

1. **Download the datasets**: 
   - First, download the datasets from the [Zenodo poyect](https://zenodo.org/records/15639492) and place them in the same folder as the Jupyter Notebook `graficas.ipynb`.
   - Once the datasets are downloaded, you can execute the notebook by clicking "Run All".

2. **Generate specific graphs or statistical results**:
   - If you wish to view the specific graphs for the transgender subgroup or the statistical results, the process is the same. You will just need to use the following files:
     - `graficas_trans.ipynb` for the transgender-specific graphs.
     - `analisis_estadistico.ipynb` for the statistical results.

3. **Re-run toxicity analysis**:
   - If you want to go further back and re-run the toxicity analysis using the [Perspective API](https://perspectiveapi.com/), you will need to request an API_KEY from Perspective API.
   - Insert the API_KEY in the designated section of the file `analisis_toxicidad.py`.

4. **Collect data from scratch**:
   - To run the entire project from scratch, you can collect the data using the following files:
     - `descarga_datos_aleatorios.py` for random tweets.
     - `descarga_datos_colectivo.py` for LGTBIQ+ related tweets. 
       - The keywords for this dataset were introduced in four blocks (since the string was too long, resulting in information loss), and this file contains the final block of the four. For more information, please contact the authors.
   - Before running these files, make sure to register on [twitterapi.io](https://twitterapi.io/), obtain your API_KEY, and replace it in the appropriate section in the scripts.

Following these steps will allow you to replicate the entire process and generate the same results and visualizations.

---



### Versión en español:

# Discurso de odio en Twitter: Análisis de la LGTBIQ-fobia antes y después de Elon Musk

Este repositorio contiene el código utilizado para la implementación del Trabajo de Fin de Grado en la Facultad de Informática de la Universidad Complutense de Madrid.

## Visión general del proyecto

El proyecto, titulado **"Discurso de odio en Twitter: Análisis de la LGTBIQ-fobia antes y después de Elon Musk"**, es el primer estudio en español que analiza la situación de la LGTBIQ-fobia en Twitter tras la compra de la plataforma por Elon Musk. El marco temporal abarca desde 2015 hasta 2024, centrando su estudio en los tuits en español del 28 de junio de cada año (Día del Orgullo). Para este análisis, se recopiló un conjunto de datos de 653.000 tuits relacionados con la comunidad LGTBIQ+. Como punto de referencia para la comparación, también se recopiló un segundo conjunto de datos de 395.000 tuits aleatorios.

## Recopilación de datos

Los conjuntos de datos se recolectaron utilizando [twitterapi.io](https://twitterapi.io/) y el código del repositorio que comienza con `descarga_datos`. Estos conjuntos de datos incluyen:

- **Tuits relacionados con la comunidad LGTBIQ+** (653.000)
- **Tuits aleatorios** (395.000)

Estos conjuntos de datos pueden encontrarse en el siguiente enlace: [Poyecto Zenodo](https://zenodo.org/records/15639492)

## Clasificación de toxicidad

Los conjuntos de datos recopilados fueron clasificados utilizando la [Perspective API](https://perspectiveapi.com/) para analizar el nivel de toxicidad. Este proceso de clasificación está gestionado por el código en el archivo `analisis_toxicidad.py`.

## Análisis estadístico

El análisis estadístico de los datos se realiza en el archivo `analisis_estadistico.ipynb`, que incluye métricas clave y comparaciones.

## Gráficas y visualizaciones

Las gráficas y visualizaciones se generan en los archivos `graficas.ipynb` y `graficas_trans.ipynb`, siendo este último un subanálisis relacionado con las personas trans.

---

### Archivos en este repositorio:

1. **LICENSE**: Información de la licencia del proyecto.
2. **README.md**: Este archivo, que proporciona una visión general del repositorio.
3. **analisis_estadistico.ipynb**: Contiene el análisis estadístico de los conjuntos de datos.
4. **analisis_toxicidad.py**: Script para la clasificación de toxicidad usando la Perspective API.
5. **descarga_datos_aleatorios.py**: Código para descargar tuits aleatorios.
6. **descarga_datos_colectivo.py**: Código para descargar tuits relacionados con la comunidad LGTBIQ+.
7. **graficas.ipynb**: Notebook para generar gráficas y visualizaciones.
8. **graficas_trans.ipynb**: Notebook para visualizar datos relacionados con personas trans.
9. **thesis.pdf**: Contiene el Trabajo de Fin de Grado, detallando la investigación y análisis realizados.
---

# Instrucciones para replicar el trabajo

Para replicar el trabajo, por favor siga las siguientes instrucciones:

1. **Descargar los conjuntos de datos**: 
   - En primer lugar, descarga los conjuntos de datos desde el [Poyecto Zenodo](https://zenodo.org/records/15639492) y colócalos en la misma carpeta que el Jupyter Notebook `graficas.ipynb`.
   - Una vez descargados los datasets, puedes ejecutar el notebook haciendo clic en "Run All".

2. **Generar gráficos específicos o resultados estadísticos**:
   - Si deseas ver los gráficos específicos para el subgrupo trans o los resultados estadísticos, el procedimiento es el mismo. Solo necesitarás usar los siguientes archivos:
     - `graficas_trans.ipynb` para los gráficos específicos del subgrupo trans.
     - `analisis_estadistico.ipynb` para los resultados estadísticos.

3. **Reejecutar el análisis de toxicidad**:
   - Si deseas ir más atrás y reejecutar el análisis de toxicidad usando la API de Perspective, necesitarás solicitar una API_KEY de [Perspective API](https://perspectiveapi.com/).
   - Inserta la API_KEY en la sección correspondiente del archivo `analisis_toxicidad.py` y ejecútalo para obtener los valores de toxicidad.

4. **Recolectar los datos desde cero**:
   - Para ejecutar el proyecto completo desde cero, puedes recolectar los datos usando los siguientes archivos:
     - `descarga_datos_aleatorios.py` para tuits aleatorios.
     - `descarga_datos_colectivo.py` para tuits relacionados con LGTBIQ+.
       - Las palabras clave para este conjunto de datos fueron introducidas en cuatro bloques (debido a que la cadena era demasiado larga y se perdía información), y este archivo contiene el último bloque de los cuatro. Para más información, por favor contacta a los autores.
   - Antes de ejecutar estos archivos, asegúrate de registrarte en [twitterapi.io](https://twitterapi.io/), obtener tu API_KEY y reemplazarla en la sección correspondiente de los scripts.

Siguiendo estos pasos podrás replicar todo el proceso y generar los mismos resultados y visualizaciones.

