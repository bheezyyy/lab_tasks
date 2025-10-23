# ЛР5 — JSON и конвертации (JSON↔CSV, CSV→XLSX)

## Быстрый старт
```bash
# активация виртуалки и установка зависимостей
python -m venv .venv && . .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Конверсии (запускайте из корня python_labs/)
python - <<'PY'
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx
json_to_csv('data/samples/people.json', 'data/out/people_from_json.csv')
csv_to_json('data/samples/people.csv', 'data/out/people_from_csv.json')
csv_to_xlsx('data/samples/people.csv', 'data/out/people.xlsx')
print('Готово')
PY
```

## Допущения
- Кодировка строго UTF-8.
- Для JSON→CSV заголовки формируются как **алфавитно отсортированное объединение всех ключей**.
- Для CSV→JSON первая строка — обязательный заголовок; значения сохраняются **как строки**.
- XLSX создаётся лист **Sheet1**, автоширина ≥ 8 символов.

## Проверка сценариев
- JSON→CSV: сравните число строк (N объектов → N строк CSV + 1 заголовок).
- CSV→JSON: сравните множество ключей и количество объектов.
- CSV→XLSX: откройте файл `data/out/people.xlsx` в Excel/LibreOffice и проверьте ширины колонок.

## Структура
См. дерево репозитория в условии. В этой сборке созданы минимальные примеры и артефакты.
