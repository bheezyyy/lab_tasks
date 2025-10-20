import sys, argparse
from pathlib import Path
from collections import Counter
from src.lab04.io_txt_csv import read_text, write_csv
from src.lib.text import normalize, tokenize, top_n

def freq(text): return Counter(tokenize(normalize(text)))
def sort_freq(f): return sorted(f.items(), key=lambda x: (-x[1], x[0]))

def main():
    a = argparse.ArgumentParser()
    a.add_argument("--in", dest="files", nargs="+", default=["data/lab04/input.txt"])
    a.add_argument("--out", default="data/lab04/report.csv")
    a.add_argument("--encoding", default="utf-8")
    a.add_argument("--per-file")
    a.add_argument("--total")
    p = a.parse_args()

    try:
        if len(p.files) == 1 and not p.per_file:
            f = freq(read_text(p.files[0], p.encoding))
            write_csv(sort_freq(f), p.out, ("word","count"))
            print(f"Всего слов: {sum(f.values())}\nУникальных: {len(f)}")
            for w,c in top_n(f): print(f"{w}:{c}")
        else:
            allf, per = Counter(), []
            for file in p.files:
                f = freq(read_text(file, p.encoding)); allf += f
                for w,c in sort_freq(f): per.append((Path(file).name,w,c))
            if p.per_file:
                per.sort(key=lambda x:(x[0],-x[2],x[1]))
                write_csv(per,p.per_file,("file","word","count"))
            if p.total: write_csv(sort_freq(allf),p.total,("word","count"))
    except FileNotFoundError as e:
        sys.exit(f"Arquivo não encontrado: {e.filename}")
    except UnicodeDecodeError:
        sys.exit("Erro de codificação — tente --encoding cp1251")

if __name__ == "__main__": main()
