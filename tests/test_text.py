import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


# --- Testes Normalize ---
@pytest.mark.parametrize(
    "source, expected",
    [
        ("Olá   Mundo", "olá mundo"),
        ("TESTE", "teste"),
        ("", ""),
    ],
)
def test_normalize(source, expected):
    assert normalize(source) == expected


# --- Testes Tokenize ---
def test_tokenize():
    text = "olá mundo, teste"
    assert tokenize(text) == ["olá", "mundo", "teste"]


# --- Testes Count Freq ---
def test_count_freq():
    tokens = ["banana", "maçã", "banana"]
    expected = {"banana": 2, "maçã": 1}
    assert count_freq(tokens) == expected


# --- Testes Top N ---
def test_top_n():
    freq = {"a": 10, "b": 20, "c": 5}
    # Deve retornar 'b' (20) e 'a' (10)
    assert top_n(freq, 2) == [("b", 20), ("a", 10)]


def test_top_n_tie():
    # Teste de desempate alfabético
    freq = {"z": 5, "a": 5}
    assert top_n(freq, 2) == [("a", 5), ("z", 5)]
