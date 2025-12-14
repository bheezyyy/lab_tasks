import re
from collections import Counter


def normalize(text: str) -> str:
    text = text.replace("Ё", "Е").replace("ё", "е").casefold()
    return re.sub(r"\s+", " ", text).strip()


def tokenize(text: str) -> list[str]:
    return re.findall(r"\w+(?:-\w+)*", text)


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:n]
