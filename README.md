# Hate Speech on Twitter: Analysis of LGBTIQ-phobia Before and After Elon Musk

This repository contains the code used for the implementation of the Final Degree Project at the Faculty of Computer Science of the Complutense University of Madrid.

## Project Overview

The project, titled **"Hate Speech in Twitter: Analysis of LGTBIQ-phobia Before and After Elon Musk"**, is the first study in Spanish that analyzes the situation of LGTBIQ-phobia on Twitter following Musk’s acquisition of the platform. The study focuses on tweets in Spanish from June 28th of each year (Pride Day), ranging from 2015 to 2024. For this analysis, a dataset of 650,000 tweets related to the LGTBIQ+ community was collected. As a benchmark for comparison, a second dataset of 390,100 random tweets was collected.

## Dataset Collection

The datasets were obtained using **twitterapi.io** and the code in the repository starting with `descarga_datos`. These datasets include:

- **LGTBIQ+ related tweets** (650,000)
- **Random tweets** (390,100)

These datasets can be found in the following link: [Poyecto Zenodo](https://zenodo.org/records/15488984)

## Toxicity Classification

The collected datasets were classified using the **Perspective API** to analyze the level of toxicity. This classification process is handled by the code in the `analisis_toxicidad.py` file.

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


---



### Versión en español:

# Discurso de odio en Twitter: Análisis de la LGTBIQ-fobia antes y después de Elon Musk

Este repositorio contiene el código utilizado para la implementación del Trabajo de Fin de Grado en la Facultad de Informática de la Universidad Complutense de Madrid.

## Visión general del proyecto

El proyecto, titulado **"Discurso de odio en Twitter: Análisis de la LGTBIQ-fobia antes y después de Elon Musk"**, es el primer estudio en español que analiza la situación de la LGTBIQ-fobia en Twitter tras la compra de la plataforma por Elon Musk. El marco temporal abarca desde 2015 hasta 2024, centrando su estudio en los tuits en español del 28 de junio de cada año (Día del Orgullo). Para este análisis, se recopiló un conjunto de datos de 650,000 tuits relacionados con la comunidad LGTBIQ+. Como punto de referencia para la comparación, también se recopiló un segundo conjunto de datos de 390,100 tuits aleatorios.

## Recopilación de datos

Los conjuntos de datos se recolectaron utilizando **twitterapi.io** y el código del repositorio que comienza con `descarga_datos`. Estos conjuntos de datos incluyen:

- **Tuits relacionados con la comunidad LGTBIQ+** (650,000)
- **Tuits aleatorios** (390,100)

Estos conjuntos de datos pueden encontrarse en el siguiente enlace: [Poyecto Zenodo](https://zenodo.org/records/15488984)

## Clasificación de toxicidad

Los conjuntos de datos recopilados fueron clasificados utilizando la **Perspective API** para analizar el nivel de toxicidad. Este proceso de clasificación está gestionado por el código en el archivo `analisis_toxicidad.py`.

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

---
