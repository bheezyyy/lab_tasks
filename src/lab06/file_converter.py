import argparse
import csv
import json
import os
import sys

# Try importing openpyxl for Excel support (handles missing library gracefully)
try:
    from openpyxl import Workbook

    HAS_OPENPYXL = True
except ImportError:
    HAS_OPENPYXL = False


def ensure_dir(file_path):
    """Creates the output directory if it doesn't exist."""
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)


# --- Logic for json2csv ---
def convert_json_to_csv(input_path, output_path):
    try:
        with open(input_path, "r", encoding="utf-8") as jf:
            data = json.load(jf)

        # Ensure data is a list of dicts
        if not isinstance(data, list) or not data:
            print("Error: JSON must be a list of objects.", file=sys.stderr)
            return

        ensure_dir(output_path)
        with open(output_path, "w", newline="", encoding="utf-8") as cf:
            writer = csv.DictWriter(cf, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        print(f"converted: {input_path} -> {output_path}")

    except Exception as e:
        print(f"Error (json2csv): {e}", file=sys.stderr)


# --- Logic for csv2json ---
def convert_csv_to_json(input_path, output_path):
    try:
        data = []
        with open(input_path, "r", encoding="utf-8") as cf:
            reader = csv.DictReader(cf)
            for row in reader:
                data.append(row)

        ensure_dir(output_path)
        with open(output_path, "w", encoding="utf-8") as jf:
            json.dump(data, jf, indent=4, ensure_ascii=False)
        print(f"converted: {input_path} -> {output_path}")

    except Exception as e:
        print(f"Error (csv2json): {e}", file=sys.stderr)


# --- Logic for csv2xlsx ---
def convert_csv_to_xlsx(input_path, output_path):
    if not HAS_OPENPYXL:
        print(
            "Error: 'openpyxl' not installed. Run 'pip install openpyxl'",
            file=sys.stderr,
        )
        return

    try:
        wb = Workbook()
        ws = wb.active

        with open(input_path, "r", encoding="utf-8") as cf:
            reader = csv.reader(cf)
            for row in reader:
                ws.append(row)

        ensure_dir(output_path)
        wb.save(output_path)
        print(f"converted: {input_path} -> {output_path}")

    except Exception as e:
        print(f"Error (csv2xlsx): {e}", file=sys.stderr)


# --- Main CLI Setup ---
def main():
    parser = argparse.ArgumentParser(description="Lab 06: Data Converters")
    subparsers = parser.add_subparsers(
        dest="cmd", required=True, help="Conversion commands"
    )

    # 1. json2csv
    p1 = subparsers.add_parser("json2csv")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    # 2. csv2json
    p2 = subparsers.add_parser("csv2json")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    # 3. csv2xlsx
    p3 = subparsers.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()

    # Pre-check input file existence
    if not os.path.exists(args.input):
        print(f"Error: Input file '{args.input}' not found.", file=sys.stderr)
        sys.exit(1)

    # Dispatcher
    if args.cmd == "json2csv":
        convert_json_to_csv(args.input, args.output)
    elif args.cmd == "csv2json":
        convert_csv_to_json(args.input, args.output)
    elif args.cmd == "csv2xlsx":
        convert_csv_to_xlsx(args.input, args.output)


if __name__ == "__main__":
    main()
