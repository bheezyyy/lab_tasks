import argparse
import sys
import os
import re
from collections import Counter


def run_cat(filepath, number_lines):
    """
    Lê um arquivo e imprime o conteúdo.
    Se number_lines for True, adiciona números de linha.
    """
    try:
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Arquivo não encontrado: {filepath}")

        with open(filepath, "r", encoding="utf-8") as f:
            for i, line in enumerate(f, 1):
                if number_lines:
                    # Imprime número da linha + tabulação + conteúdo
                    print(f"{i}\t{line}", end="")
                else:
                    print(line, end="")
            print()  # Garante uma quebra de linha no final

    except Exception as e:
        print(f"Erro ao ler arquivo: {e}", file=sys.stderr)


def run_stats(filepath, top_n):
    """
    Conta a frequência das palavras em um arquivo de texto.
    """
    try:
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Arquivo não encontrado: {filepath}")

        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()

        # Limpeza simples: remove pontuação e converte para minúsculas
        # O regex [^\w\s] remove tudo que não for letra ou espaço
        clean_text = re.sub(r"[^\w\s]", "", text).lower()
        words = clean_text.split()

        # Conta as palavras
        counter = Counter(words)
        most_common = counter.most_common(top_n)

        print(f"--- Top {top_n} Palavras Mais Frequentes ---")
        for word, count in most_common:
            print(f"{word}: {count}")

    except Exception as e:
        print(f"Erro ao analisar estatísticas: {e}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(description="Lab 06: Ferramentas de Texto CLI")
    subparsers = parser.add_subparsers(
        dest="command", required=True, help="Comandos disponíveis"
    )

    # --- Comando: cat ---
    # Uso: cat --input <arquivo> [-n]
    cat_parser = subparsers.add_parser("cat", help="Imprimir conteúdo do arquivo")
    cat_parser.add_argument(
        "--input", required=True, help="Caminho para o arquivo de texto"
    )
    cat_parser.add_argument("-n", action="store_true", help="Numerar as linhas")

    # --- Comando: stats ---
    # Uso: stats --input <arquivo> [--top 3]
    stats_parser = subparsers.add_parser(
        "stats", help="Analisar frequência de palavras"
    )
    stats_parser.add_argument(
        "--input", required=True, help="Caminho para o arquivo de texto"
    )
    stats_parser.add_argument(
        "--top", type=int, default=5, help="Número de palavras a exibir"
    )

    args = parser.parse_args()

    if args.command == "cat":
        run_cat(args.input, args.n)
    elif args.command == "stats":
        run_stats(args.input, args.top)


if __name__ == "__main__":
    main()
    import os

os.makedirs("data/samples", exist_ok=True)

texto = """
Python is powerful.
Python is simple.
I live for the code/.
"""

with open("data/samples/text.txt", "w", encoding="utf-8") as f:
    f.write(texto.strip())

print("Arquivo de texto criado em: data/samples/text.txt")
