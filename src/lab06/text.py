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