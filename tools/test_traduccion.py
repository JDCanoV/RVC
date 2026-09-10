from pathlib import Path

from tools.song_processing.transcribir import transcribir_audio
from tools.song_processing.traducir import traducir_segmentos_contextuales


audio = Path(
    r"resultados_cancion\separacion\voz\Olivia Rodrigo - deja vu (Official Video)_vocals.wav"
)

print("=" * 70)
print("PRUEBA WHISPER MEDIUM + MARIANMT")
print("=" * 70)

# --------------------------------------------------
# 1. WHISPER MEDIUM
# --------------------------------------------------

print("\n[1/2] Transcribiendo con Whisper Medium...")

resultado = transcribir_audio(
    audio,
    idioma="en",
)

segmentos = resultado["segments"]

print(
    f"\nSegmentos detectados por Whisper: "
    f"{len(segmentos)}"
)

# --------------------------------------------------
# 2. MARIANMT
# --------------------------------------------------

print("\n[2/2] Traduciendo segmentos...")

traducciones = traducir_segmentos_contextuales(
    segmentos
)

# --------------------------------------------------
# RESULTADO
# --------------------------------------------------

print("\n" + "=" * 70)
print("RESULTADO WHISPER MEDIUM + MARIANMT")
print("=" * 70)

for i, segmento in enumerate(traducciones, start=1):

    print(
        f"\n{i}. "
        f"[{segmento['start']:.2f}s - "
        f"{segmento['end']:.2f}s]"
    )

    print("Original:", segmento["original"])
    print("Traducción:", segmento["traduccion"])

print("\n" + "=" * 70)
print(
    f"TOTAL SEGMENTOS TRADUCIDOS: "
    f"{len(traducciones)}"
)
print("=" * 70)