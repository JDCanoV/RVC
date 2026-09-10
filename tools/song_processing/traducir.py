from transformers import MarianMTModel, MarianTokenizer

MODELO_TRADUCCION = "Helsinki-NLP/opus-mt-en-es"

_tokenizer = None
_modelo = None


def cargar_modelo():
    global _tokenizer, _modelo

    if _tokenizer is None or _modelo is None:
        print("Cargando modelo de traducción...")

        _tokenizer = MarianTokenizer.from_pretrained(
            MODELO_TRADUCCION
        )

        _modelo = MarianMTModel.from_pretrained(
            MODELO_TRADUCCION
        )

    return _tokenizer, _modelo


def traducir_texto(texto):
    tokenizer, modelo = cargar_modelo()

    entradas = tokenizer(
        texto,
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=512,
    )

    salida = modelo.generate(
        **entradas,
        max_length=512,
        num_beams=5,
        early_stopping=True,
    )

    traduccion = tokenizer.decode(
        salida[0],
        skip_special_tokens=True,
    )

    return " ".join(
        traduccion.strip().split()
    )


def traducir_segmentos_contextuales(segmentos):
    resultados = []

    total = len(segmentos)

    for i, segmento in enumerate(segmentos):

        texto_actual = segmento.get(
            "text", ""
        ).strip()

        start = float(
            segmento.get("start", 0)
        )

        end = float(
            segmento.get("end", 0)
        )

        if not texto_actual:
            continue

        if end <= start:
            continue

        # Contexto ORIGINAL en inglés.
        texto_anterior = ""

        if i > 0:
            texto_anterior = segmentos[i - 1].get(
                "text", ""
            ).strip()

        texto_siguiente = ""

        if i < total - 1:
            texto_siguiente = segmentos[i + 1].get(
                "text", ""
            ).strip()

        # Por ahora MarianMT traduce SOLO el segmento actual.
        # El contexto se conserva en el JSON para usarlo
        # posteriormente con un traductor contextual real.
        traduccion = traducir_texto(
            texto_actual
        )

        resultados.append({
            "start": start,
            "end": end,
            "original": texto_actual,
            "traduccion": traduccion,
            "contexto_anterior": texto_anterior,
            "contexto_posterior": texto_siguiente,
        })

        print(
            f"[{start:.2f}s - {end:.2f}s] "
            f"{texto_actual} -> {traduccion}"
        )

    return resultados