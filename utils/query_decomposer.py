import re


CONNECTOR_PATTERNS = [
    r"\.\s+",
    r";\s*",
    r",\s+luego\s+",
    r"\s+luego\s+",
    r"\s+despues\s+",
    r"\s+despu[eé]s\s+",
]

ACTION_START_PATTERN = re.compile(
    r"^(agrega|anade|anadir|modifica|actualiza|elimina|borra|consulta|revisa|busca|explica|resuelve|calcula|dime|cual es|cuanto es|que es)\b",
    flags=re.IGNORECASE
)


def split_compound_request(user_message: str):
    normalized = user_message.strip()

    if not normalized:
        return []

    parts = [normalized]

    for pattern in CONNECTOR_PATTERNS:
        new_parts = []

        for part in parts:
            split_parts = [
                piece.strip(" ,")
                for piece in re.split(pattern, part)
                if piece.strip(" ,")
            ]
            new_parts.extend(split_parts)

        parts = new_parts

    final_parts = []

    for part in parts:
        split_on_and = _split_on_action_connector(part)

        for piece in split_on_and:
            cleaned_piece = piece.strip(" ,")

            if cleaned_piece:
                final_parts.append(cleaned_piece)

    return final_parts or [normalized]


def _split_on_action_connector(text: str):
    matches = list(
        re.finditer(
            r"\s+y\s+",
            text,
            flags=re.IGNORECASE
        )
    )

    if not matches:
        return [text]

    chunks = []
    start = 0

    for match in matches:
        candidate = text[match.end():].strip()

        if ACTION_START_PATTERN.match(candidate):
            chunks.append(text[start:match.start()].strip())
            start = match.end()

    chunks.append(text[start:].strip())

    return chunks
