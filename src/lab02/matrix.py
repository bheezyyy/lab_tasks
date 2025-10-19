import ast
from typing import List, Union

Number = Union[int, float]

# ===== Helper =====

def check_rectangular(mat: List[List[Number]]) -> None:
    """
    Ensure all rows have the same length.
    
    Raises:
        ValueError: if the matrix is ragged.
    """
    if not mat:
        return
    row_len = len(mat[0])
    for row in mat:
        if len(row) != row_len:
            raise ValueError("torn matrix")


# ===== Functions =====

def transpose(mat: List[List[Number]]) -> List[List[Number]]:
    """Swap rows and columns of a rectangular matrix."""
    if not mat:
        return []
    check_rectangular(mat)
    return [[row[i] for row in mat] for i in range(len(mat[0]))]


def row_sums(mat: List[List[Number]]) -> List[Number]:
    """Return a list with sum of each row."""
    if not mat:
        return []
    check_rectangular(mat)
    return [sum(row) for row in mat]


def col_sums(mat: List[List[Number]]) -> List[Number]:
    """Return a list with sum of each column."""
    if not mat:
        return []
    check_rectangular(mat)
    return [sum(row[i] for row in mat) for i in range(len(mat[0]))]


# ===== Input Parsing =====

def parse_matrix_input(input_str: str) -> List[List[Number]]:
    """
    Parse a full matrix input as a Python literal (list/tuple of rows).
    Raises ValueError if matrix is invalid or ragged.
    """
    try:
        mat = ast.literal_eval(input_str)
        if not isinstance(mat, list):
            raise ValueError("torn matrix")
        for row in mat:
            if not isinstance(row, (list, tuple)):
                raise ValueError("torn matrix")
        return mat
    except (ValueError, SyntaxError):
        raise ValueError("Invalid input. Please enter a valid matrix.")


# ===== Interactive Menu =====

def main():
    print("=== Lab 02: Matrix Operations ===")
    print("Choose an operation:")
    print("1 — transpose")
    print("2 — row_sums")
    print("3 — col_sums")
    print("0 — Exit")

    while True:
        choice = input("\nEnter your choice: ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        elif choice in {"1", "2", "3"}:
            matrix_str = input(
                "Enter full matrix (Python lists/tuples), e.g. [[1,2], [3,4]]: "
            )
            try:
                matrix = parse_matrix_input(matrix_str)
                if choice == "1":
                    print("Result (transposed):", transpose(matrix))
                elif choice == "2":
                    print("Result (row sums):", row_sums(matrix))
                elif choice == "3":
                    print("Result (column sums):", col_sums(matrix))
            except ValueError as ve:
                print(ve)

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
