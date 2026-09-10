from pathlib import Path

from tools.song_processing.pipeline import (
    procesar_cancion,
    guardar_resultado,
)


audio = Path(
    r"C:\Users\jdcan\Downloads\Olivia Rodrigo - deja vu (Official Video).wav"
)

carpeta_salida = Path(
    "resultados_cancion"
)

resultado = procesar_cancion(
    audio,
    carpeta_salida,
    idioma="en",
)

ruta_json = (
    carpeta_salida /
    "cancion_procesada.json"
)

guardar_resultado(
    resultado,
    ruta_json,
)

print("\n" + "=" * 60)
print("RESULTADO FINAL")
print("=" * 60)

print("\nVoz:")
print(resultado["voz"])

print("\nInstrumental:")
print(resultado["instrumental"])

print(
    f"\nSegmentos: "
    f"{len(resultado['traducciones'])}"
)

print("\nPrimeras traducciones:")

for segmento in resultado["traducciones"][:10]:
    print(
        f"\n[{segmento['start']:.2f}s - "
        f"{segmento['end']:.2f}s]"
    )
    print("Original:", segmento["original"])
    print("Traducción:", segmento["traduccion"])