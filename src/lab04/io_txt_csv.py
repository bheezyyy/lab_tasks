from pathlib import Path
import csv

def ensure_parent_dir(path):
    p = Path(path).parent
    p.mkdir(parents=True, exist_ok=True)

def read_text(path, encoding="utf-8"):
    return Path(path).read_text(encoding=encoding)

def write_csv(rows, path, header=None):
    rows = list(rows)
    if header and any(len(r) != len(header) for r in rows):
        raise ValueError("Tamanhos diferentes entre linha e cabeçalho.")
    ensure_parent_dir(path)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header: w.writerow(header)
        w.writerows(rows)
