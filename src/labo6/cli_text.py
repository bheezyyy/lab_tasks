import argparse
import sys
import os
from pathlib import Path

# Adiciona o diretório pai ao sys.path para importar lib.text
# Certifique-se de que a pasta 'lib' e o arquivo 'text.py' existam no local correto
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

# Importa as funções da biblioteca (assumindo que lab03 ou similar está em lib.text)
try:
    from lib.text import normalize, tokenize, count_freq, top_n, print_table
except ImportError:
    # Fallback caso a lib não esteja configurada, apenas para evitar crash imediato
    # Se você já tem o arquivo lib/text.py, isso não será necessário.
    pass

def main():
    parser = argparse.ArgumentParser(description="Utilitários CLI do Laboratório nº 6")
    subparsers = parser.add_subparsers(dest="command")

    # Subcomando cat
    cat_parser = subparsers.add_parser("cat", help="Exibir o conteúdo do arquivo")
    cat_parser.add_argument("--input", required=True, help="Caminho do arquivo de entrada")
    cat_parser.add_argument("-n", action="store_true", help="Numerar as linhas")

    # Subcomando stats
    stats_parser = subparsers.add_parser("stats", help="Frequência das palavras")
    stats_parser.add_argument("--input", required=True, help="Caminho do arquivo de entrada")
    stats_parser.add_argument("--top", type=int, default=5, help="Número de palavras a exibir")

    args = parser.parse_args()

    # Se o subcomando não for especificado, mostra a ajuda e sai.
    if not args.command:
        parser.print_help()
        return

    if args.command == "cat":
        """Implementação do comando cat"""
        file_path = args.input

        if not Path(file_path).exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                for num, line in enumerate(file, start=1):
                    if args.n:
                        print(f"{num}: {line}", end="")
                    else:
                        print(line, end="")

        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")

    elif args.command == "stats":
        """Implementação do comando stats"""
        file_path = args.input

        if not Path(file_path).exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()

            # Processamento do texto usando as funções importadas de lib.text
            normalize_text = normalize(text)
            tokens = tokenize(normalize_text)
            freq = count_freq(tokens)
            top_words = top_n(freq, args.top)
            print_table(top_words)

        except Exception as e:
            print(f"Erro ao processar o arquivo: {e}")
            # Dica extra caso o erro seja de importação
            if "name 'normalize' is not defined" in str(e):
                print("Dica: Verifique se as funções (normalize, tokenize, etc.) foram importadas corretamente de lib.text")

    else:
        parser.print_help()
        return


if __name__ == "__main__":
    main()