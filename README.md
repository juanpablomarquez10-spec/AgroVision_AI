🌱 AgroVision IA

Sistema de clasificación de enfermedades en hojas de tomate mediante Deep Learning y visión por computadora.

Proyecto académico individual para la asignatura de Deep Learning.

1. Descripción del proyecto

AgroVision IA es una aplicación que utiliza modelos de aprendizaje profundo para clasificar imágenes de hojas de tomate en tres categorías:

Tizón temprano (Early blight).

Tizón tardío (Late blight).

Hoja sana (Healthy).

El proyecto implementa y compara dos enfoques de clasificación: una red neuronal convolucional (CNN) y MobileNetV2 mediante transferencia de aprendizaje.

2. Problema y objetivo

Las enfermedades de las plantas de tomate pueden afectar la productividad de los cultivos. La identificación de síntomas mediante imágenes puede servir como apoyo para reconocer posibles problemas fitosanitarios.

Objetivo general: desarrollar y evaluar dos modelos de Deep Learning para clasificar imágenes de hojas de tomate y comparar su desempeño.

3. Conjunto de datos

El experimento se realizó con un conjunto de 1.495 imágenes pertenecientes a tres categorías:

Categoría

Descripción

Tomato___Early_blight

Tizón temprano

Tomato___Late_blight

Tizón tardío

Tomato___healthy

Hoja sana

La distribución utilizada fue la siguiente:

Conjunto

Número de imágenes

Entrenamiento

1.046

Validación

224

Prueba

225

Total

1.495

La división se realizó utilizando la semilla aleatoria 42. Las imágenes del conjunto de datos no están incluidas en el repositorio y deben prepararse por separado para volver a entrenar los modelos.

4. Modelos y resultados

Los dos modelos se evaluaron utilizando el mismo conjunto de prueba.

Modelo

Exactitud

Pérdida

CNN básica

76,44 %

0,5803

MobileNetV2

93,33 %

0,2107

En este experimento, MobileNetV2 obtuvo una exactitud superior a la CNN básica por 16,89 puntos porcentuales.

Estos resultados corresponden al conjunto de prueba utilizado. El rendimiento puede variar con imágenes externas que presenten diferentes condiciones de iluminación, fondos, ángulos o síntomas.

5. Estructura del repositorio

Los principales archivos y carpetas publicados son:

Archivo o carpeta

Descripción

descargar_datos.py

Descarga o preparación del conjunto de datos.

verificar_datos.py

Verificación de las categorías del conjunto de datos.

dividir_datos.py

División de los datos en entrenamiento, validación y prueba.

entrenar_modelo.py

Entrenamiento de la CNN básica.

entrenar_mobilenet.py

Entrenamiento de MobileNetV2.

predecir_imagen.py

Predicción sobre una imagen.

interfaz_agrovision.py

Interfaz de la aplicación AgroVision IA.

generar_comparacion.py

Comparación de los modelos.

generar_evidencias.py

Generación de archivos de evidencia.

requirements.txt

Dependencias de Python.

modelos/

Modelos entrenados publicados.

resultados/

Métricas y gráficas de la CNN.

resultados_mobilenet/

Métricas y gráficas de MobileNetV2.

evidencias/

Informes, comparación y capturas de la aplicación.

6. Tecnologías utilizadas

Python.

TensorFlow y Keras.

NumPy y pandas.

scikit-learn.

Matplotlib.

Pillow.

GitHub para el almacenamiento y la documentación del proyecto.

7. Instalación y ejecución

7.1. Requisitos previos

Python compatible con las versiones de las dependencias.

Conexión a internet para instalar las dependencias.

Los archivos del repositorio descargados en el equipo.

7.2. Descargar el proyecto

En GitHub, abre el repositorio y selecciona Code → Download ZIP. Descomprime el archivo y abre PowerShell en la carpeta del proyecto.

7.3. Crear y activar un entorno virtual

En Windows PowerShell, ejecuta los siguientes comandos por separado:


python -m venv .venv
.\.venv\Scripts\Activate.ps1


Si PowerShell impide la activación por la política de ejecución, consulta la documentación de Python para Windows antes de modificar la configuración del sistema.

7.4. Instalar las dependencias

python -m pip install -r requirements.txt

7.5. Ejecutar la aplicación

La interfaz utiliza el archivo interfaz_agrovision.py. Antes de ejecutarla, verifica que los modelos entrenados estén disponibles en modelos/ y que las rutas definidas en el código coincidan con la estructura del proyecto.

Desde la carpeta donde se encuentra el archivo de la interfaz, ejecuta:

python interfaz_agrovision.py

Si el archivo está dentro de la carpeta src, utiliza:

python .\src\interfaz_agrovision.py

La ejecución correcta depende de que las dependencias, los modelos y las rutas requeridas estén configurados adecuadamente.

7.6. Entrenamiento de los modelos

Para volver a entrenar los modelos es necesario disponer de las imágenes del conjunto de datos y verificar las rutas utilizadas por los scripts. No es necesario repetir el entrenamiento para consultar los resultados de los modelos ya entrenados incluidos en el repositorio.

8. Evidencias y reproducibilidad

En la carpeta evidencias/ se encuentran los archivos de comparación, el informe y las capturas de las pruebas de la aplicación.

Los resultados publicados permiten documentar el experimento y comparar los dos modelos. Para reproducir completamente el entrenamiento, es necesario preparar el conjunto de datos y utilizar un entorno compatible con las dependencias.

9. Alcance y limitaciones

AgroVision IA es un proyecto académico experimental que se limita a tres categorías de hojas de tomate. El modelo puede producir predicciones incorrectas, especialmente ante imágenes diferentes de las utilizadas durante el entrenamiento.

El porcentaje de confianza de una predicción no garantiza que el diagnóstico sea correcto. La aplicación no sustituye la evaluación de un especialista agrícola.

10. Autor

Juan Pablo Tejada Márquez

Proyecto académico individual para la asignatura de Deep Learning.
