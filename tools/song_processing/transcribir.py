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
    mapa_idiomas = {
        "inglés": "en",
        "español": "es",
        "francés": "fr",
        "alemán": "de",
        "italiano": "it",
        "portugués": "pt",
        "en": "en",
        "es": "es",
        "fr": "fr",
        "de": "de",
        "it": "it",
        "pt": "pt",
    }

    if isinstance(idioma, (list, tuple)):
        idioma = idioma[0] if idioma else "en"

    idioma = str(idioma).strip().lower()
    idioma = mapa_idiomas.get(idioma, idioma)

    print(
        f"[Whisper] Idioma recibido: {idioma}",
        flush=True,
    )

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