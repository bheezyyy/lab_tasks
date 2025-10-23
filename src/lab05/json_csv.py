from __future__ import annotations
import json
import csv
from pathlib import Path
from typing import List, Dict, Any

__all__ = ["json_to_csv", "csv_to_json"]

def _ensure_ext(path: Path, *allowed: str) -> None:
    if path.suffix.lower() not in allowed:
        raise ValueError(f"Неверный тип файла для {path.name}: ожидается {', '.join(allowed)}")

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл (список словарей) в CSV.
    - Поддерживает список словарей [{...}, {...}]
    - Пустые или неподдерживаемые структуры -> ValueError
    - Заполняет отсутствующие поля пустыми строками
    - Кодировка UTF-8
    - Порядок колонок — **алфавитно** по объединению всех ключей
    """
    jpath = Path(json_path)
    cpath = Path(csv_path)

    _ensure_ext(jpath, ".json")
    _ensure_ext(cpath, ".csv")

    if not jpath.exists():
        raise FileNotFoundError(str(jpath))

    with jpath.open(encoding="utf-8") as jf:
        try:
            data = json.load(jf)
        except json.JSONDecodeError as e:
            raise ValueError(f"Некорректный JSON: {e}") from e

    if not isinstance(data, list) or not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура (ожидается непустой список словарей)")
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("JSON должен быть списком словарей")

    # Собираем все ключи
    all_keys = sorted({k for row in data for k in row.keys()})

    # Запись CSV
    with cpath.open("w", newline="", encoding="utf-8") as cf:
        writer = csv.DictWriter(cf, fieldnames=all_keys)
        writer.writeheader()
        for row in data:
            # отсутствующие поля -> ""
            writer.writerow({k: _stringify(row.get(k, "")) for k in all_keys})

def _stringify(v: Any) -> str:
    if v is None:
        return ""
    if isinstance(v, (str, int, float)):
        return str(v)
    # Для вложенных структур сериализуем в компактный JSON
    return json.dumps(v, ensure_ascii=False, separators=(",", ":"))

def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    - Первая строка обязана быть заголовком
    - Значения сохраняются как строки
    - json.dump(..., ensure_ascii=False, indent=2)
    """
    cpath = Path(csv_path)
    jpath = Path(json_path)

    _ensure_ext(cpath, ".csv")
    _ensure_ext(jpath, ".json")

    if not cpath.exists():
        raise FileNotFoundError(str(cpath))

    # Пытаемся распознать диалект и проверить пустоту
    with cpath.open(encoding="utf-8") as f:
        sample = f.read(4096)
        if not sample.strip():
            raise ValueError("Пустой CSV")
        f.seek(0)
        try:
            dialect = csv.Sniffer().sniff(sample)
        except csv.Error:
            # по умолчанию запятая
            dialect = csv.excel

        reader = csv.reader(f, dialect)
        try:
            header = next(reader)
        except StopIteration:
            raise ValueError("CSV не содержит данных")
        if not header or any(h is None or h == "" for h in header):
            raise ValueError("CSV должен содержать непустой заголовок")

        f.seek(0)
        dict_reader = csv.DictReader(f, dialect=dialect)
        if dict_reader.fieldnames is None:
            raise ValueError("Не удалось определить заголовок CSV")

        rows = [ {k: (v if v is not None else "") for k, v in row.items()} for row in dict_reader ]

    # Доп. валидация на пустоту данных (не только заголовок)
    # Допускаем 0 строк, но это будет пустой список в JSON
    data: List[Dict[str, str]] = rows

    with jpath.open("w", encoding="utf-8") as jf:
        json.dump(data, jf, ensure_ascii=False, indent=2)
