import argparse
import sys
import os

# Adiciona o diretório pai ao path para importar a biblioteca
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

# Importa as funções de conversão (certifique-se de que elas estão em lib/text.py ou ajuste o import)
from lib.text import json_to_csv, csv_to_json, csv_to_xlsx


def main():
    # Descrição principal da ferramenta
    parser = argparse.ArgumentParser(description="Conversores de dados")
    sub = parser.add_subparsers(dest="cmd", help="Comandos disponíveis")

    # --- Comando: json2csv ---
    p1 = sub.add_parser("json2csv", help="Converter JSON para CSV")
    p1.add_argument("--in", dest="input", required=True, help="Arquivo de entrada (JSON)")
    p1.add_argument("--out", dest="output", required=True, help="Arquivo de saída (CSV)")

    # --- Comando: csv2json ---
    p2 = sub.add_parser("csv2json", help="Converter CSV para JSON")
    p2.add_argument("--in", dest="input", required=True, help="Arquivo de entrada (CSV)")
    p2.add_argument("--out", dest="output", required=True, help="Arquivo de saída (JSON)")

    # --- Comando: csv2xlsx ---
    p3 = sub.add_parser("csv2xlsx", help="Converter CSV para XLSX")
    p3.add_argument("--in", dest="input", required=True, help="Arquivo de entrada (CSV)")
    p3.add_argument("--out", dest="output", required=True, help="Arquivo de saída (XLSX)")

    args = parser.parse_args()

    # Verifica qual comando foi chamado e executa a função correspondente
    try:
        if args.cmd == "json2csv":
            json_to_csv(args.input, args.output)
            print(f"Sucesso: {args.input} convertido para {args.output}")
            
        elif args.cmd == "csv2json":
            csv_to_json(args.input, args.output)
            print(f"Sucesso: {args.input} convertido para {args.output}")
            
        elif args.cmd == "csv2xlsx":
            csv_to_xlsx(args.input, args.output)
            print(f"Sucesso: {args.input} convertido para {args.output}")
            
        else:
            # Se nenhum comando for passado, exibe a ajuda
            parser.print_help()
            
    except Exception as e:
        print(f"Erro durante a conversão: {e}")


if __name__ == "__main__":
    main()