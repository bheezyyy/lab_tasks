import re
from collections import Counter


def clean(text):
    """
    Limpa o texto removendo pontuações e convertendo para minúsculas.
    """
    return re.sub(r"[^a-zA-ZÀ-ÿ0-9\s]", "", text).lower()


def split_words(text):
    """
    Divide o texto em palavras individuais.
    """
    return text.split()


def word_freq(words):
    """
    Conta a frequência de cada palavra e retorna um dicionário (Counter).
    """
    return Counter(words)


def top_words(freq, n=5):
    """
    Retorna as n palavras mais frequentes.
    """
    return freq.most_common(n)


def main():
    txt = input("Digite o texto: ")
    words = split_words(clean(txt))
    total = len(words)
    unique = len(set(words))
    freq = word_freq(words)
    top = top_words(freq)

    print(f"\nTotal de palavras: {total}")
    print(f"Palavras únicas: {unique}")
    print("\nTop 5 palavras:")
    print(f'{"Palavra":^12} | {"Contagem":^8}')
    print("-" * 23)
    for w, c in top:
        print(f"{w:^12} | {c:^8}")


if __name__ == "__main__":
    main()
