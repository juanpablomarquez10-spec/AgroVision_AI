from pathlib import Path
import json
import shutil
import csv
from datetime import datetime

# Ruta principal del proyecto
BASE = Path(__file__).resolve().parent.parent
DESTINO = BASE / "evidencias"

DESTINO.mkdir(parents=True, exist_ok=True)

print("=" * 55)
print("GENERADOR DE EVIDENCIAS - AGROVISION AI")
print("=" * 55)

# 1. Resumen del dataset dividido
carpeta_datos = BASE / "data_divididos"
resumen = {
    "fecha_generacion": datetime.now().isoformat(timespec="seconds"),
    "proyecto": "AgroVision AI",
    "dataset": {}
}

if carpeta_datos.exists():
    for particion in ["entrenamiento", "validacion", "prueba"]:
        carpeta = carpeta_datos / particion

        if not carpeta.exists():
            # Compatibilidad si las carpetas tienen nombres sin tilde
            alternativas = {
                "entrenamiento": "train",
                "validacion": "val",
                "prueba": "test"
            }
            carpeta = carpeta_datos / alternativas[particion]

        if carpeta.exists():
            resumen["dataset"][particion] = {}

            for clase in sorted(carpeta.iterdir()):
                if clase.is_dir():
                    imagenes = [
                        f for f in clase.iterdir()
                        if f.is_file() and f.suffix.lower()
                        in [".jpg", ".jpeg", ".png", ".bmp", ".webp"]
                    ]
                    resumen["dataset"][particion][clase.name] = len(imagenes)

    (DESTINO / "resumen_dataset.json").write_text(
        json.dumps(resumen, indent=4, ensure_ascii=False),
        encoding="utf-8"
    )
    print("[OK] Resumen del dataset")
else:
    print("[AVISO] No se encontró data_divididos")

# 2. Copiar métricas, gráficos e historiales existentes
recursos = [
    ("resultados", "CNN"),
    ("resultados_mobilenet", "MobileNetV2")
]

for carpeta_nombre, modelo in recursos:
    origen = BASE / carpeta_nombre

    if not origen.exists():
        print(f"[AVISO] No existe {carpeta_nombre}")
        continue

    destino_modelo = DESTINO / modelo
    destino_modelo.mkdir(exist_ok=True)

    for archivo in origen.iterdir():
        if archivo.is_file() and archivo.suffix.lower() in [
            ".json", ".png", ".csv", ".txt"
        ]:
            shutil.copy2(archivo, destino_modelo / archivo.name)
            print(f"[OK] {modelo}/{archivo.name}")

# 3. Crear comparación a partir de las métricas guardadas
rutas_metricas = [
    ("CNN", DESTINO / "CNN" / "metricas_prueba.json"),
    ("MobileNetV2", DESTINO / "MobileNetV2" / "metricas_prueba.json")
]

comparacion = []

for modelo, archivo in rutas_metricas:
    if archivo.exists():
        try:
            datos = json.loads(archivo.read_text(encoding="utf-8"))
            comparacion.append({
                "modelo": modelo,
                "metricas": datos
            })
        except (json.JSONDecodeError, OSError) as error:
            print(f"[AVISO] No se pudo leer {archivo.name}: {error}")

(DESTINO / "comparacion_modelos.json").write_text(
    json.dumps(comparacion, indent=4, ensure_ascii=False),
    encoding="utf-8"
)

# 4. Generar informe de evidencias
lineas = [
    "# Evidencias del proyecto AgroVision AI",
    "",
    f"Fecha de generación: {datetime.now():%Y-%m-%d %H:%M:%S}",
    "",
    "## Dataset",
    ""
]

if resumen["dataset"]:
    for particion, clases in resumen["dataset"].items():
        total = sum(clases.values())
        lineas.append(f"### {particion}: {total} imágenes")
        for clase, cantidad in clases.items():
            lineas.append(f"- {clase}: {cantidad} imágenes")
        lineas.append("")
else:
    lineas.append(
        "No se pudo generar el resumen. Verificar data_divididos."
    )

lineas += [
    "## Resultados guardados",
    "",
    "- CNN: revisar carpeta `CNN`.",
    "- MobileNetV2: revisar carpeta `MobileNetV2`.",
    "- Comparación: `comparacion_modelos.json`.",
    "",
    "## Interfaz gráfica",
    "",
    "Guardar aquí una captura real de la interfaz funcionando, "
    "por ejemplo `prueba_interfaz_agrovision.png`.",
    "",
    "Nota: las métricas corresponden a los archivos generados "
    "durante los experimentos; este script no vuelve a entrenar "
    "ni modifica los modelos."
]

(DESTINO / "informe_evidencias.md").write_text(
    "\n".join(lineas), encoding="utf-8"
)

print()
print("Proceso terminado.")
print(f"Carpeta de evidencias: {DESTINO}")
print("Revisa los avisos anteriores para detectar archivos faltantes.")