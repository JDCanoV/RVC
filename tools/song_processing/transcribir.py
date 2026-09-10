import whisper

MODELO_WHISPER = "medium"

_modelo_whisper = None


def cargar_whisper():
    global _modelo_whisper

    if _modelo_whisper is None:
        print("Cargando modelo Whisper...")
        _modelo_whisper = whisper.load_model(MODELO_WHISPER)

    return _modelo_whisper


def transcribir_audio(ruta_audio, idioma="en"):
    modelo = cargar_whisper()

    resultado = modelo.transcribe(
        str(ruta_audio),
        language=idioma,
        task="transcribe",
        fp16=False,
        temperature=0,
        condition_on_previous_text=True,
        word_timestamps=True,
    )
    return resultado