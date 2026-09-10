from pathlib import Path

from tools.song_processing.separar import separar_voz_instrumental


audio = Path(
    r"C:\Users\jdcan\Downloads\Olivia Rodrigo - deja vu (Official Video).wav"
)

salida = Path("resultados_cancion") / "separacion"

voz, instrumental = separar_voz_instrumental(
    audio,
    salida,
)

print("\n" + "=" * 60)
print("RESULTADO FINAL")
print("=" * 60)

print("Voz:")
print(voz)

print("\nInstrumental:")
print(instrumental)