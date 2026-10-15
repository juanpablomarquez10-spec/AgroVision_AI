
from pathlib import Path
import json
import csv

BASE = Path(__file__).resolve().parent.parent
EVIDENCIAS = BASE / "evidencias"

archivos = [
    ("CNN desde cero", EVIDENCIAS / "CNN" / "metricas_prueba.json"),
    ("MobileNetV2", EVIDENCIAS / "MobileNetV2" / "metricas_prueba.json"),
]

filas = []

for nombre, ruta in archivos:
    if not ruta.exists():
        print(f"[AVISO] Falta el archivo: {ruta}")
        continue

    datos = json.loads(ruta.read_text(encoding="utf-8"))
    informe = datos["informe_clasificacion"]

    filas.append({
        "Modelo": nombre,
        "Exactitud (%)": round(datos["exactitud_prueba"] * 100, 2),
        "Perdida": round(datos["perdida_prueba"], 4),
        "Precision macro (%)": round(
            informe["macro avg"]["precision"] * 100, 2
        ),
        "Recall macro (%)": round(
            informe["macro avg"]["recall"] * 100, 2
        ),
        "F1 macro (%)": round(
            informe["macro avg"]["f1-score"] * 100, 2
        ),
        "Imagenes de prueba": int(
            informe["macro avg"]["support"]
        )
    })

salida = EVIDENCIAS / "comparacion_modelos.csv"

with salida.open("w", newline="", encoding="utf-8-sig") as archivo:
    columnas = [
        "Modelo", "Exactitud (%)", "Perdida",
        "Precision macro (%)", "Recall macro (%)",
        "F1 macro (%)", "Imagenes de prueba"
    ]
    escritor = csv.DictWriter(archivo, fieldnames=columnas)
    escritor.writeheader()
    escritor.writerows(filas)

print("\nCOMPARACION DE MODELOS")
print("-" * 75)

for fila in filas:
    print(
        f'{fila["Modelo"]}: '
        f'Exactitud={fila["Exactitud (%)"]}% | '
        f'F1 macro={fila["F1 macro (%)"]}% | '
        f'Perdida={fila["Perdida"]}'
    )

if len(filas) == 2:
    mejora = filas[1]["Exactitud (%)"] - filas[0]["Exactitud (%)"]
    print(f"\nMejora de exactitud: {mejora:.2f} puntos porcentuales")

print(f"\n[OK] Archivo guardado en: {salida}")

