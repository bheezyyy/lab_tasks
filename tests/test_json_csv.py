import pytest
import json
import csv
from src.lab05.json_csv import json_to_csv, csv_to_json


def test_json_to_csv(tmp_path):
    # Cria arquivos temporários
    json_file = tmp_path / "data.json"
    csv_file = tmp_path / "data.csv"

    data = [{"nome": "Ana", "idade": 20}]
    json_file.write_text(json.dumps(data), encoding="utf-8")

    json_to_csv(str(json_file), str(csv_file))

    assert csv_file.exists()
    content = csv_file.read_text(encoding="utf-8")
    assert "Ana" in content


def test_csv_to_json(tmp_path):
    csv_file = tmp_path / "data.csv"
    json_file = tmp_path / "data.json"

    csv_file.write_text("nome,idade\nCarlos,30", encoding="utf-8")

    csv_to_json(str(csv_file), str(json_file))

    assert json_file.exists()
    with open(json_file, encoding="utf-8") as f:
        res = json.load(f)
    assert res[0]["nome"] == "Carlos"


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        json_to_csv("arquivo_fantasma.json", "out.csv")
