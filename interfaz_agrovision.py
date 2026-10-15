from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

import numpy as np
import tensorflow as tf
from PIL import Image, ImageTk, UnidentifiedImageError

BASE_DIR = Path(__file__).resolve().parent.parent
RUTA_MODELO = BASE_DIR / "modelos" / "mobilenetv2_tomate.keras"
TAMANO_IMAGEN = (180, 180)

CLASES = [
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___healthy",
]

NOMBRES = {
    "Tomato___Early_blight": "Tizon temprano",
    "Tomato___Late_blight": "Tizon tardio",
    "Tomato___healthy": "Hoja sana",
}


class AgroVisionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AgroVision AI - Clasificador de hojas de tomate")
        self.root.geometry("720x700")
        self.root.minsize(600, 600)

        self.modelo = None
        self.imagen_tk = None

        contenedor = ttk.Frame(root, padding=20)
        contenedor.pack(fill="both", expand=True)

        ttk.Label(
            contenedor,
            text="AgroVision AI",
            font=("Segoe UI", 24, "bold")
        ).pack(pady=(0, 4))

        ttk.Label(
            contenedor,
            text="Clasificacion de enfermedades en hojas de tomate",
            font=("Segoe UI", 11)
        ).pack(pady=(0, 18))

        self.boton = ttk.Button(
            contenedor,
            text="Seleccionar fotografia",
            command=self.seleccionar_imagen
        )
        self.boton.pack(pady=6)

        self.etiqueta_imagen = ttk.Label(
            contenedor,
            text="Selecciona una imagen JPG, JPEG o PNG",
            anchor="center"
        )
        self.etiqueta_imagen.pack(fill="both", expand=True, pady=12)

        self.resultado = ttk.Label(
            contenedor,
            text="La prediccion aparecera aqui",
            font=("Segoe UI", 15, "bold"),
            anchor="center",
            justify="center"
        )
        self.resultado.pack(pady=12)

        self.detalle = ttk.Label(
            contenedor,
            text="",
            font=("Segoe UI", 11),
            justify="left"
        )
        self.detalle.pack(pady=8)

        ttk.Label(
            contenedor,
            text="Herramienta experimental; no reemplaza un diagnostico agronomico.",
            wraplength=620,
            justify="center"
        ).pack(pady=(12, 0))

    def seleccionar_imagen(self):
        ruta = filedialog.askopenfilename(
            title="Seleccionar una hoja de tomate",
            filetypes=[
                ("Imagenes", "*.jpg *.jpeg *.png"),
                ("Todos los archivos", "*.*")
            ]
        )

        if not ruta:
            return

        try:
            with Image.open(ruta) as original:
                imagen = original.convert("RGB")
                vista = imagen.copy()
                vista.thumbnail((420, 300))

                self.imagen_tk = ImageTk.PhotoImage(vista)
                self.etiqueta_imagen.configure(
                    image=self.imagen_tk,
                    text=""
                )

                imagen_modelo = imagen.resize(TAMANO_IMAGEN)
                arreglo = np.asarray(imagen_modelo, dtype=np.float32)
                lote = np.expand_dims(arreglo, axis=0)

        except (OSError, UnidentifiedImageError) as error:
            messagebox.showerror(
                "Error de imagen",
                f"No fue posible abrir la imagen.\n{error}"
            )
            return

        try:
            if self.modelo is None:
                if not RUTA_MODELO.is_file():
                    raise FileNotFoundError(
                        f"No se encontro el modelo:\n{RUTA_MODELO}"
                    )

                self.resultado.configure(
                    text="Cargando modelo..."
                )
                self.root.update_idletasks()
                self.modelo = tf.keras.models.load_model(RUTA_MODELO)

            probabilidades = self.modelo.predict(lote, verbose=0)[0]

            if len(probabilidades) != len(CLASES):
                raise ValueError(
                    "El modelo no devuelve las tres categorias esperadas."
                )

            indice = int(np.argmax(probabilidades))
            nombre = NOMBRES[CLASES[indice]]
            confianza = float(probabilidades[indice]) * 100

            self.resultado.configure(
                text=f"Prediccion: {nombre}\n"
                     f"Probabilidad estimada: {confianza:.2f}%"
            )

            lineas = ["Resultados por categoria:"]
            for clase, valor in zip(CLASES, probabilidades):
                lineas.append(
                    f"• {NOMBRES[clase]}: {float(valor) * 100:.2f}%"
                )

            self.detalle.configure(text="\n".join(lineas))

        except Exception as error:
            messagebox.showerror(
                "Error de prediccion",
                f"No fue posible generar la prediccion.\n{error}"
            )
            self.resultado.configure(text="No se pudo generar la prediccion")
            self.detalle.configure(text="")


if __name__ == "__main__":
    ventana = tk.Tk()
    app = AgroVisionApp(ventana)
    ventana.mainloop()