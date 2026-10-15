🌱 AgroVision_AI

Sistema de clasificación de enfermedades en hojas de tomate mediante Deep Learning y visión por computadora.

1. Descripción del proyecto

AgroVision_AI es un proyecto académico individual que busca clasificar imágenes de hojas de tomate para identificar dos tipos de enfermedades y distinguir las hojas sanas. Se implementaron y evaluaron dos enfoques de aprendizaje profundo: una red neuronal convolucional (CNN) y MobileNetV2 mediante transferencia de aprendizaje.

2. Planteamiento del problema

Las enfermedades de los cultivos de tomate pueden afectar su productividad y calidad. La identificación de síntomas a partir de imágenes puede apoyar la detección temprana y la toma de decisiones agrícolas. Este proyecto explora el uso de modelos de Deep Learning para automatizar esa clasificación.

3. Objetivo general

Desarrollar y evaluar modelos de Deep Learning capaces de clasificar imágenes de hojas de tomate en tres categorías.

4. Datos utilizados

El conjunto de datos utilizado en el experimento contiene 1.495 imágenes, distribuidas en tres categorías:

Tomato___Early_blight: tizón temprano.

Tomato___Late_blight: tizón tardío.

Tomato___healthy: hojas sanas.

Distribución registrada:

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

Los datos se dividieron con una semilla de 42 para facilitar la reproducibilidad.

5. Modelos y resultados

Se evaluaron dos modelos sobre el conjunto de prueba:

Modelo

Exactitud

Pérdida

CNN básica

76,44 %

0,5803

MobileNetV2

93,33 %

0,2107

En el experimento realizado, MobileNetV2 obtuvo la mayor exactitud. Estos resultados corresponden al conjunto de prueba utilizado y no garantizan el mismo rendimiento con imágenes externas.

6. Tecnologías utilizadas

Python.

TensorFlow y Keras.

NumPy y scikit-learn.

Matplotlib.

Procesamiento y clasificación de imágenes.

Git y GitHub.

7. Estructura del proyecto

src/: scripts de preparación, entrenamiento, evaluación, predicción e interfaz.

data/: imágenes originales.

data_divididos/: conjuntos de entrenamiento, validación y prueba.

modelos/: modelos entrenados.

resultados/: métricas y gráficas de la CNN.

resultados_mobilenet/: métricas y gráficas de MobileNetV2.

evidencias/: comparación de modelos e informe de evidencias.

Los datos, modelos y resultados se encuentran en el entorno local de desarrollo; su disponibilidad en GitHub depende de los archivos que se publiquen en el repositorio.

8. Estado del proyecto

Se completaron la preparación y división de los datos, el entrenamiento de la CNN y MobileNetV2, la evaluación sobre el conjunto de prueba y la generación de archivos de comparación y evidencias.

La siguiente etapa consiste en verificar la predicción con imágenes nuevas, revisar la interfaz y organizar los entregables para la presentación académica.

9. Autor

Juan Pablo Tejada Marquez

Proyecto académico individual para la asignatura de Deep Learning.
