from pathlib import Path
import json

from .separar import separar_voz_instrumental
from .transcribir import transcribir_audio
from .traducir import traducir_segmentos_contextuales


def procesar_cancion(ruta_audio, carpeta_salida, idioma="en"):
    ruta_audio = Path(ruta_audio).resolve()
    carpeta_salida = Path(carpeta_salida).resolve()

    carpeta_salida.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("PROCESANDO CANCIÓN")
    print("=" * 60)

    # ---------------------------------------------------------
    # 1. SEPARAR VOZ E INSTRUMENTAL
    # ---------------------------------------------------------
    print("\n[1/3] Separando voz e instrumental...")

    voz, instrumental = separar_voz_instrumental(
        ruta_audio,
        carpeta_salida / "separacion",
    )

    # ---------------------------------------------------------
    # 2. TRANSCRIBIR LA VOZ AISLADA
    # ---------------------------------------------------------
    print("\n[2/3] Transcribiendo voz...")

    resultado_whisper = transcribir_audio(
        voz,
        idioma=idioma,
    )

    segmentos = resultado_whisper["segments"]

    print(f"Segmentos detectados: {len(segmentos)}")

    # ---------------------------------------------------------
    # 3. TRADUCIR
    # ---------------------------------------------------------
    print("\n[3/3] Traduciendo...")

    traducciones = traducir_segmentos_contextuales(
        segmentos
    )

    # ---------------------------------------------------------
    # RESULTADO FINAL
    # ---------------------------------------------------------
    resultado_final = {
        "audio_original": str(ruta_audio),
        "voz": str(voz),
        "instrumental": str(instrumental),
        "segmentos": segmentos,
        "traducciones": traducciones,
    }

    return resultado_final


def guardar_resultado(resultado, ruta_salida):
    ruta_salida = Path(ruta_salida)

    ruta_salida.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        ruta_salida,
        "w",
        encoding="utf-8",
    ) as archivo:
        json.dump(
            resultado,
            archivo,
            ensure_ascii=False,
            indent=4,
        )

    print(f"\nResultado guardado en: {ruta_salida}")