from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

import numpy as np
import tensorflow as tf
from PIL import Image, ImageTk, UnidentifiedImageError


# Rutas del proyecto
BASE_DIR = Path(__file__).resolve().parent
RUTA_MODELO = BASE_DIR / "modelos" / "mobilenetv2_tomate.keras"

# Configuración de las imágenes
TAMANO_IMAGEN = (180, 180)

# Clases utilizadas durante el entrenamiento
CLASES = [
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___healthy",
]

# Nombres legibles para mostrar los resultados
NOMBRES = {
    "Tomato___Early_blight": "Tizón temprano",
    "Tomato___Late_blight": "Tizón tardío",
    "Tomato___healthy": "Hoja sana",
}


class AgroVisionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AgroVision IA - Clasificador de hojas de tomate")
        self.root.geometry("720x700")
        self.root.minsize(600, 600)

        self.modelo = None
        self.imagen_tk = None

        # Contenedor principal
        contenedor = ttk.Frame(root, padding=20)
        contenedor.pack(fill="both", expand=True)

        # Título
        ttk.Label(
            contenedor,
            text="AgroVision IA",
            font=("Segoe UI", 24, "bold")
        ).pack(pady=(0, 4))

        ttk.Label(
            contenedor,
            text="Clasificación de enfermedades en hojas de tomate",
            font=("Segoe UI", 11)
        ).pack(pady=(0, 18))

        # Botón para seleccionar una fotografía
        self.boton = ttk.Button(
            contenedor,
            text="Seleccionar fotografía",
            command=self.seleccionar_imagen
        )
        self.boton.pack(pady=6)

        # Área para visualizar la imagen seleccionada
        self.etiqueta_imagen = ttk.Label(
            contenedor,
            text="Selecciona una imagen JPG, JPEG o PNG",
            anchor="center"
        )
        self.etiqueta_imagen.pack(
            fill="both",
            expand=True,
            pady=12
        )

        # Resultado de la predicción
        self.resultado = ttk.Label(
            contenedor,
            text="La predicción aparecerá aquí",
            font=("Segoe UI", 15, "bold"),
            anchor="center",
            justify="center"
        )
        self.resultado.pack(pady=12)

        # Detalle de probabilidades por categoría
        self.detalle = ttk.Label(
            contenedor,
            text="",
            font=("Segoe UI", 11),
            justify="left"
        )
        self.detalle.pack(pady=8)

        # Aviso sobre el alcance del sistema
        ttk.Label(
            contenedor,
            text=(
                "Herramienta experimental; no reemplaza "
                "un diagnóstico agronómico."
            ),
            wraplength=620,
            justify="center"
        ).pack(pady=(12, 0))

    def seleccionar_imagen(self):
        ruta = filedialog.askopenfilename(
            title="Seleccionar una hoja de tomate",
            filetypes=[
                ("Imágenes", "*.jpg *.jpeg *.png"),
                ("Todos los archivos", "*.*")
            ]
        )

        if not ruta:
            return

        # Abrir y preparar la imagen
        try:
            with Image.open(ruta) as original:
                imagen = original.convert("RGB")

                # Crear una copia para mostrar en la interfaz
                vista = imagen.copy()
                vista.thumbnail((420, 300))

                self.imagen_tk = ImageTk.PhotoImage(vista)
                self.etiqueta_imagen.configure(
                    image=self.imagen_tk,
                    text=""
                )

                # Preparar la imagen para el modelo
                imagen_modelo = imagen.resize(TAMANO_IMAGEN)

                arreglo = np.asarray(
                    imagen_modelo,
                    dtype=np.float32
                )

                lote = np.expand_dims(arreglo, axis=0)

        except (OSError, UnidentifiedImageError) as error:
            messagebox.showerror(
                "Error de imagen",
                f"No fue posible abrir la imagen.\n{error}"
            )
            return

        # Cargar el modelo y realizar la predicción
        try:
            if self.modelo is None:
                if not RUTA_MODELO.is_file():
                    raise FileNotFoundError(
                        "No se encontró el modelo entrenado:\n"
                        f"{RUTA_MODELO}\n\n"
                        "Verifica que el archivo "
                        "'mobilenetv2_tomate.keras' esté "
                        "dentro de la carpeta 'modelos'."
                    )

                self.resultado.configure(
                    text="Cargando modelo..."
                )
                self.detalle.configure(text="")
                self.root.update_idletasks()

                self.modelo = tf.keras.models.load_model(
                    RUTA_MODELO
                )

            probabilidades = self.modelo.predict(
                lote,
                verbose=0
            )[0]

            if len(probabilidades) != len(CLASES):
                raise ValueError(
                    "El modelo no devuelve las tres categorías "
                    "esperadas. Verifica las clases del entrenamiento."
                )

            # Obtener la clase con mayor probabilidad
            indice = int(np.argmax(probabilidades))
            clase_predicha = CLASES[indice]
            nombre = NOMBRES[clase_predicha]
            confianza = float(probabilidades[indice]) * 100

            self.resultado.configure(
                text=(
                    f"Predicción: {nombre}\n"
                    f"Probabilidad estimada: {confianza:.2f}%"
                )
            )

            # Mostrar las probabilidades de todas las clases
            lineas = ["Resultados por categoría:"]

            for clase, valor in zip(CLASES, probabilidades):
                lineas.append(
                    f"• {NOMBRES[clase]}: "
                    f"{float(valor) * 100:.2f}%"
                )

            self.detalle.configure(
                text="\n".join(lineas)
            )

        except Exception as error:
            messagebox.showerror(
                "Error de predicción",
                "No fue posible generar la predicción.\n\n"
                f"Detalle: {error}"
            )

            self.resultado.configure(
                text="No se pudo generar la predicción"
            )
            self.detalle.configure(text="")


if __name__ == "__main__":
    ventana = tk.Tk()
    app = AgroVisionApp(ventana)
    ventana.mainloop()
