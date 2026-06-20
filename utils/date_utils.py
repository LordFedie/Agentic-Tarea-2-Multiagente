import re


MONTHS = {
    "enero": "01",
    "febrero": "02",
    "marzo": "03",
    "abril": "04",
    "mayo": "05",
    "junio": "06",
    "julio": "07",
    "agosto": "08",
    "septiembre": "09",
    "setiembre": "09",
    "octubre": "10",
    "noviembre": "11",
    "diciembre": "12",
}


DATE_PATTERN = re.compile(
    r"\b(?P<day>\d{1,2})\s+de\s+"
    r"(?P<month>enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|setiembre|octubre|noviembre|diciembre)"
    r"\s+de\s+(?P<year>\d{4})\b",
    flags=re.IGNORECASE
)


def normalize_dates_in_text(text: str) -> str:

    def replace_match(match):
        day = int(match.group("day"))
        month = MONTHS[match.group("month").lower()]
        year = match.group("year")

        return f"{year}-{month}-{day:02d}"

    return DATE_PATTERN.sub(replace_match, text)
