import argparse
import sys
import os
import re
from collections import Counter


# --- Logic for the 'cat' command ---
def run_cat(filepath, number_lines):
    """
    Reads a file and prints it.
    If number_lines (-n) is True, it adds line numbers.
    """
    try:
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")

        with open(filepath, "r", encoding="utf-8") as f:
            for i, line in enumerate(f, 1):
                if number_lines:
                    print(f"{i}\t{line}", end="")
                else:
                    print(line, end="")
            print()  # Ensure clean newline at end

    except Exception as e:
        print(f"Error processing file: {e}", file=sys.stderr)


# --- Logic for the 'stats' command ---
def run_stats(filepath, top_n):
    """
    Counts word frequencies in a text file.
    """
    try:
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")

        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()

        # Basic cleaning: lowercase and remove punctuation
        clean_text = re.sub(r"[^\w\s]", "", text).lower()
        words = clean_text.split()

        counter = Counter(words)
        most_common = counter.most_common(top_n)

        print(f"--- Top {top_n} Words ---")
        for word, count in most_common:
            print(f"{word}: {count}")

    except Exception as e:
        print(f"Error analyzing stats: {e}", file=sys.stderr)


# --- Main CLI Setup ---
def main():
    parser = argparse.ArgumentParser(description="Lab 06: Text Analysis CLI")
    subparsers = parser.add_subparsers(
        dest="command", required=True, help="Available commands"
    )

    # 1. Setup 'cat' command
    # Usage: cat --input <file> [-n]
    cat_parser = subparsers.add_parser("cat", help="Print file content to console")
    cat_parser.add_argument("--input", required=True, help="Path to text file")
    cat_parser.add_argument("-n", action="store_true", help="Show line numbers")

    # 2. Setup 'stats' command
    # Usage: stats --input <file> [--top 5]
    stats_parser = subparsers.add_parser("stats", help="Show word frequency stats")
    stats_parser.add_argument("--input", required=True, help="Path to text file")
    stats_parser.add_argument(
        "--top", type=int, default=5, help="Number of top words to show"
    )

    args = parser.parse_args()

    # Execute based on command
    if args.command == "cat":
        run_cat(args.input, args.n)
    elif args.command == "stats":
        run_stats(args.input, args.top)


if __name__ == "__main__":
    main()
