# Laboratorio - Implementando un modelo de Machine Learning

**Este Laboratorio está inspirado en la unidad 1 del curso [Introduction to Machine Learning in Production (DeepLearning.AI)](https://www.coursera.org/learn/introduction-to-machine-learning-in-production/home/welcome).**

Para comenzar deben haber bajado todos los archivos a una carpeta y en el terminal de Anaconda llegar a ese directorio.

```
.
└── pd-mds-2022-lab (este directorio)
    ├── model (acá irán nuestros modelos)
    ├── 00_nyc-taxi-model.ipynb
    ├── 01_server.ipynb
    ├── 02_client.ipynb
    └── requirements.txt (dependencias de Python)
```
 
 
## Pasos previos usando Conda
 
### Prerequisito: Tener [conda](https://docs.conda.io/en/latest/) instalado en tu computador.
 
Vamos a usar Conda para construir un entorno virtual nuevo.
 
### 1. Creando el entorno virtual (Virtual Environment)
 
Asumiremos que tenemos instalado conda. El primer paso es crear un nuevo enviroment para desarrollar. Para crear uno usando Python 3.7 debemos ejecutar el siguiente comando:
 
```bash
conda create --name pd-mds-2022-lab python=3.8
```
 
Luego debemos activarlo usando el comando:
 
```bash
conda activate pd-mds-2022-lab
```
 
Todo el trabajo que realicemos con este código será en este entorno. Así que al trabajarcon estos archivos siempre tiene que estar activo el ambiente pd-mds-2022-lab.
 
### 2. Instalando las dependencias usando PIP 
 
Antes de seguir, verifica que en el terminal de Anaconda estés dentro del directorio `pd-mds-2022-lab`, el cual incluye el archivo `requirements.txt`. Este archivo enlista todas las dependencias necesarias y podemos usarlo para instalarlas todas:
 
```bash
pip install -r requirements.txt
```
 
Este comando puede demorar un rato dependiendo de la velocidad del computador y la de la conexión a Internet. Una vez que termine ya está listo todo para comenzar una sesión de Jupyter Lab o Notebook.

Luego debemos enlazar el kernel de jupyter lab a nuestro nuevo enviroment:

```bash
python -m ipykernel install --user --name pd-mds-2022-lab
```

 
### 3. Iniciando Jupyter Lab
 
Jupyter lab debería haber quedado instalado en el paso anterior, así que basta con escribir:

```bash
jupyter lab
```

### 4. Generando modelo de ML

El notebook que genera el modelo se puede ejecutar en su totalidad desde [Google Colab](https://colab.research.google.com/drive/1U71oPoyaaZJN2oniiHl_Re5W8T9LRZpA?usp=sharing).
