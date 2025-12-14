import re
from collections import Counter


def normalize(text: str) -> str:
    """Normaliza o texto: minúsculas e remove espaços extras."""
    if not text:
        return ""
    # Remove caracteres especiais se necessário, ajusta espaços e lowercase
    text = text.lower().strip()
    text = re.sub(r"\s+", " ", text)
    return text


def tokenize(text: str) -> list[str]:
    """Quebra o texto em palavras (tokens)."""
    if not text:
        return []
    # Remove pontuação básica para toquenizar limpo
    clean_text = re.sub(r"[^\w\s]", "", text)
    return clean_text.split()


def count_freq(tokens: list[str]) -> dict[str, int]:
    """Conta a frequência de cada palavra."""
    return dict(Counter(tokens))


def top_n(freq: dict[str, int], n: int) -> list[tuple[str, int]]:
    """Retorna as N palavras mais frequentes. Desempate por ordem alfabética."""
    # Ordena por contagem (desc) e depois por palavra (asc) para desempate
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]
