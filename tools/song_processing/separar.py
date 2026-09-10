from pathlib import Path
import tempfile

from tools.pymss_webui import pymss_separate


def separar_voz_instrumental(ruta_audio, carpeta_salida):
    ruta_audio = Path(ruta_audio).resolve()
    carpeta_salida = Path(carpeta_salida).resolve()

    carpeta_salida.mkdir(parents=True, exist_ok=True)

    carpeta_voz = carpeta_salida / "voz"
    carpeta_instrumental = carpeta_salida / "instrumental"

    carpeta_voz.mkdir(parents=True, exist_ok=True)
    carpeta_instrumental.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("SEPARANDO VOZ E INSTRUMENTAL")
    print("=" * 60)

    eventos = pymss_separate(
        model_name="去伴奏",
        inp_root=str(ruta_audio),
        save_root_vocal=str(carpeta_voz),
        paths=[],
        save_root_ins=str(carpeta_instrumental),
        format0="wav",
    )

    mensajes = []

    try:
        for mensaje in eventos:
            if mensaje:
                mensajes.append(mensaje)
                print(mensaje)

    finally:
        eventos.close()

    archivos_voz = list(carpeta_voz.rglob("*.wav"))
    archivos_instrumental = list(carpeta_instrumental.rglob("*.wav"))

    if not archivos_voz:
        raise FileNotFoundError(
            f"PyMSS terminó pero no se encontró la voz en: {carpeta_voz}"
        )

    if not archivos_instrumental:
        raise FileNotFoundError(
            f"PyMSS terminó pero no se encontró el instrumental en: "
            f"{carpeta_instrumental}"
        )

    voz = archivos_voz[0]
    instrumental = archivos_instrumental[0]

    print("\nSeparación terminada.")
    print("Voz:", voz)
    print("Instrumental:", instrumental)

    return voz, instrumental