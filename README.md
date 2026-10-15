AgroVision IA

Sistema de clasificación de enfermedades en hojas de tomate mediante Deep Learning y visión por computadora.

Proyecto académico individual para la asignatura de Deep Learning.

1. Descripción del proyecto

AgroVision IA es una aplicación que utiliza modelos de aprendizaje profundo para clasificar imágenes de hojas de tomate en tres categorías:

Tizón temprano: Tomato___Early_blight.

Tizón tardío: Tomato___Late_blight.

Hoja sana: Tomato___healthy.

El proyecto implementa y compara dos modelos: una red neuronal convolucional (CNN) y MobileNetV2 mediante transferencia de aprendizaje. También incluye una interfaz gráfica que permite seleccionar una imagen y consultar la predicción del modelo entrenado.

2. Problema y objetivo

Las enfermedades de las plantas de tomate pueden afectar la productividad de los cultivos. La identificación de posibles síntomas a partir de imágenes puede servir como apoyo para reconocer problemas fitosanitarios.

Objetivo general: desarrollar y evaluar dos modelos de Deep Learning para clasificar imágenes de hojas de tomate y comparar su desempeño.

3. Conjunto de datos

El experimento se realizó con un conjunto de 1.495 imágenes distribuidas en tres categorías.

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

La división se realizó utilizando la semilla aleatoria 42.

Las imágenes del conjunto de datos no están incluidas en el repositorio. Por tanto, es posible ejecutar la aplicación con los modelos entrenados publicados, pero para volver a entrenar los modelos es necesario preparar los datos y verificar las rutas que utilizan los scripts.

4. Modelos y resultados

Ambos modelos se evaluaron utilizando el mismo conjunto de prueba.

Modelo

Exactitud

Pérdida

CNN básica

76,44 %

0,5803

MobileNetV2

93,33 %

0,2107

En este experimento, MobileNetV2 superó a la CNN básica por 16,89 puntos porcentuales de exactitud.

Estos resultados corresponden a la evaluación realizada con el conjunto de prueba del proyecto. No garantizan el mismo rendimiento con fotografías externas.

5. Estructura del repositorio

Los principales archivos y carpetas son:

Archivo o carpeta

Función

descargar_datos.py

Descarga o preparación de los datos.

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

Interfaz gráfica de la aplicación.

generar_comparacion.py

Generación de la comparación entre modelos.

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

Tkinter para la interfaz gráfica.

GitHub para publicar el código, los modelos y la documentación.

7. Requisitos previos

Para ejecutar la aplicación se necesita:

Un computador con Windows y PowerShell, o un entorno compatible con Python y Tkinter.

Una instalación de Python compatible con las versiones especificadas en requirements.txt.

Conexión a internet para instalar las dependencias.

Los archivos del repositorio, incluido el modelo entrenado de MobileNetV2.

Espacio disponible para instalar las bibliotecas y cargar el modelo.

No es necesario volver a entrenar los modelos para probar la interfaz si los archivos entrenados publicados están presentes.

8. Instalación y ejecución desde GitHub

8.1. Descargar el proyecto

Abrir el repositorio: AgroVision_AI.

Seleccionar Code → Download ZIP.

Extraer el archivo ZIP mediante la opción Extraer todo.

Abrir la carpeta extraída AgroVision_AI-main.

Es importante ejecutar los comandos desde la carpeta donde están interfaz_agrovision.py y requirements.txt, no desde una carpeta superior ni desde el archivo ZIP comprimido.

8.2. Comprobar Python

Abrir PowerShell en la carpeta extraída y ejecutar:

python --version
python -m pip --version

Si Python no está disponible, será necesario instalar una versión compatible con las dependencias del proyecto y comprobar que PowerShell pueda encontrar el comando python.

8.3. Verificar los archivos necesarios

Ejecutar los siguientes comandos:

Test-Path .\interfaz_agrovision.py
Test-Path .\requirements.txt
Test-Path .\modelos\mobilenetv2_tomate.keras

Los tres comandos deben devolver True. Si alguno devuelve False, comprobar la estructura de las carpetas y que la descarga esté completa.

8.4. Crear y activar el entorno virtual

Ejecutar los comandos por separado:

python -m venv .venv
.\.venv\Scripts\Activate.ps1

Si PowerShell bloquea la activación por su política de ejecución, se puede habilitar temporalmente para la sesión actual con:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1

Este ajuste se limita a la sesión actual de PowerShell.

8.5. Instalar las dependencias

Con el entorno virtual activado, ejecutar:

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

La instalación puede tardar varios minutos. Se necesita conexión a internet y una versión de Python compatible con las dependencias fijadas en el archivo.

Para verificar las dependencias instaladas:

python -m pip check

Si aparece No broken requirements found, no se detectaron conflictos en las dependencias instaladas.

8.6. Ejecutar la interfaz gráfica

Desde la carpeta raíz del proyecto, ejecutar:

python .\interfaz_agrovision.py

La aplicación debería abrir una ventana titulada AgroVision AI - Clasificador de hojas de tomate.

Si la ventana abre, pero falla al generar una predicción, comprobar que el archivo del modelo existe en modelos/ y que la ruta definida en el código corresponde a esa ubicación.

9. Cómo probar una predicción

Una vez abierta la aplicación:

Pulsar el botón para seleccionar una fotografía.

Elegir una imagen válida de una hoja de tomate en formato JPG, JPEG o PNG.

Esperar a que el modelo procese la imagen.

Revisar la categoría predicha:

Tizón temprano.

Tizón tardío.

Hoja sana.

Consultar la probabilidad estimada de la categoría predicha y los porcentajes de las tres categorías.

Repetir la prueba con otra fotografía para verificar que la aplicación procese más de una imagen.

La probabilidad mostrada representa la salida del modelo y no constituye una garantía de que el diagnóstico sea correcto.

10. Entrenamiento y reproducibilidad

La ejecución de la interfaz y el entrenamiento son procesos diferentes.

Para probar la aplicación: basta con disponer de las dependencias y del modelo entrenado publicado.

Para repetir el entrenamiento: es necesario preparar el conjunto de datos, comprobar la estructura esperada por los scripts y ejecutar los procedimientos de entrenamiento y evaluación. La reproducción completa requiere utilizar un entorno compatible y conservar la configuración experimental correspondiente.

Los resultados publicados documentan el experimento realizado; no implican que el entrenamiento se reproduzca automáticamente al descargar el ZIP.

11. Evidencias del proyecto

La carpeta evidencias/ contiene los archivos disponibles de documentación y pruebas. Las carpetas resultados/ y resultados_mobilenet/ contienen las métricas y gráficas correspondientes a los modelos.

Se recomienda revisar estas evidencias junto con los modelos publicados y el código fuente para comprobar la correspondencia entre los resultados reportados y el experimento.

12. Alcance y limitaciones

AgroVision IA es un prototipo académico experimental limitado a tres categorías de hojas de tomate.

El modelo puede producir predicciones incorrectas cuando las imágenes presentan condiciones diferentes de las utilizadas durante el entrenamiento. La iluminación, el fondo, el ángulo, la calidad de la imagen y la presencia de síntomas distintos pueden afectar el resultado.

La aplicación no sustituye el diagnóstico ni la evaluación de un especialista agrícola.

13. Autor

Juan Pablo Tejada Márquez

Proyecto académico individual para la asignatura de Deep Learning.
