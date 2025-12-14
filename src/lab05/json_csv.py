import json
import csv
import os


def json_to_csv(src_path: str, dst_path: str):
    """Converte arquivo JSON para CSV."""
    if not os.path.exists(src_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {src_path}")

    with open(src_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            raise ValueError("JSON inválido")

    # Garante que é uma lista de dicionários
    if not isinstance(data, list) or not data:
        raise ValueError("JSON deve conter uma lista de objetos")

    keys = data[0].keys()

    with open(dst_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)


def csv_to_json(src_path: str, dst_path: str):
    """Converte arquivo CSV para JSON."""
    if not os.path.exists(src_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {src_path}")

    data = []
    with open(src_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

    with open(dst_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
