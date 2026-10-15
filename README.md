🌱 AgroVision_AI

Sistema de clasificación de enfermedades en hojas de tomate mediante Deep Learning y visión por computadora.

1. Descripción del proyecto

AgroVision_AI es un proyecto académico individual que utiliza modelos de aprendizaje profundo para clasificar imágenes de hojas de tomate en tres categorías: tizón temprano, tizón tardío y hojas sanas.

Se entrenaron y evaluaron dos modelos: una red neuronal convolucional (CNN) y MobileNetV2 mediante transferencia de aprendizaje.

2. Problema y objetivo

Las enfermedades pueden afectar la productividad de los cultivos de tomate. Este proyecto explora la clasificación automática de imágenes como apoyo a la identificación de síntomas.

Objetivo general: desarrollar y comparar dos modelos de Deep Learning para clasificar hojas de tomate en tres categorías.

3. Conjunto de datos

El experimento utilizó 1.495 imágenes distribuidas en tres clases:

Tomato___Early_blight: tizón temprano.

Tomato___Late_blight: tizón tardío.

Tomato___healthy: hojas sanas.

Conjunto

Imágenes

Entrenamiento

1.046

Validación

224

Prueba

225

Total

1.495

La división se realizó con semilla 42. Las imágenes originales y los conjuntos divididos se conservan localmente y no están incluidos en este repositorio.

4. Modelos y resultados

Ambos modelos se evaluaron sobre el mismo conjunto de prueba.

Modelo

Exactitud

Pérdida

CNN básica

76,44 %

0,5803

MobileNetV2

93,33 %

0,2107

MobileNetV2 obtuvo una exactitud superior en este experimento. Estos resultados corresponden al conjunto evaluado y no garantizan el mismo rendimiento con imágenes externas.

5. Estructura del repositorio

descargar_datos.py: descarga o preparación de datos.

verificar_datos.py: verifica las categorías disponibles.

dividir_datos.py: divide los datos en entrenamiento, validación y prueba.

entrenar_modelo.py: entrena la CNN básica.

entrenar_mobilenet.py: entrena MobileNetV2.

predecir_imagen.py: realiza predicciones sobre imágenes.

interfaz_agrovision.py: contiene la interfaz del sistema.

generar_comparacion.py: compara los resultados de los modelos.

generar_evidencias.py: genera archivos de evidencia.

modelos/: modelos entrenados publicados.

resultados/: métricas y gráficas de la CNN.

resultados_mobilenet/: métricas y gráficas de MobileNetV2.

evidencias/: informe, comparación y evidencias adicionales.

requirements.txt: dependencias de Python.

6. Tecnologías

Python

TensorFlow y Keras

NumPy y pandas

scikit-learn

Matplotlib

Pillow

GitHub

7. Instalación y ejecución

Se recomienda utilizar una versión de Python compatible con las dependencias declaradas en requirements.txt.

Crear y activar un entorno virtual:

python -m venv .venv
.\.venv\Scripts\Activate.ps1

Instalar las dependencias:

python -m pip install -r requirements.txt

Importante: antes de ejecutar los scripts de entrenamiento o predicción, verifica que los datos estén en las rutas esperadas por cada script y que los modelos entrenados se encuentren en modelos/.

Los comandos concretos para cada script pueden depender de los argumentos y las rutas definidos en su código.

8. Alcance y limitaciones

Este es un proyecto académico experimental. La clasificación se limita a las tres categorías estudiadas. El modelo puede equivocarse con imágenes externas, condiciones de iluminación diferentes u hojas con síntomas no representados en el conjunto de datos. No sustituye la evaluación de un especialista agrícola.

9. Autor

Juan Pablo Tejada Marquez

Proyecto académico individual para la asignatura de Deep Learning.
