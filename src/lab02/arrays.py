import ast
from typing import List, Tuple, Union

Number = Union[int, float]

# ===== Functions =====

def min_max(nums: List[Number]) -> Tuple[Number, Number]:
    """Return (min, max) or raise ValueError if the list is empty."""
    if not nums:
        raise ValueError
    return min(nums), max(nums)


def unique_sorted(nums: List[Number]) -> List[Number]:
    """Return sorted list of unique values."""
    return sorted(set(nums))


def flatten(mat: List[Union[List[Number], Tuple[Number, ...]]]) -> List[Number]:
    """Flatten a 2D list/tuple. Raise TypeError if any row is not list/tuple."""
    if not all(isinstance(row, (list, tuple)) for row in mat):
        raise TypeError("a row is not a row of rows of a matrix")
    flat: List[Number] = []
    for row in mat:
        flat.extend(row)
    return flat


# ===== Input Parsing =====

def parse_numbers_input(input_str: str) -> List[Number]:
    """
    Parse comma-separated numbers from user input (ints or floats).
    Example input: 3, -1, 5, 0
    """
    if not input_str.strip():
        return []
    try:
        return [float(x.strip()) if '.' in x else int(x.strip()) for x in input_str.split(',')]
    except ValueError:
        raise ValueError("Invalid input. Please enter numbers separated by commas.")


def parse_matrix_input(input_str: str) -> List[List[Number]]:
    """
    Parse a full matrix input as a Python literal (list/tuple of rows).
    Raises TypeError if any row is not a list/tuple.
    """
    try:
        mat = ast.literal_eval(input_str)
        if not isinstance(mat, list):
            raise TypeError("a row is not a row of rows of a matrix")
        for row in mat:
            if not isinstance(row, (list, tuple)):
                raise TypeError("a row is not a row of rows of a matrix")
        return mat
    except (ValueError, SyntaxError):
        raise ValueError("Invalid input. Please enter a valid matrix.")


# ===== Interactive Menu =====

def main():
    print("=== Lab 02: Collections and Matrices ===")
    print("Choose an operation:")
    print("1 — min_max")
    print("2 — unique_sorted")
    print("3 — flatten (matrix)")
    print("0 — Exit")

    while True:
        choice = input("\nEnter your choice: ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        elif choice == "1":
            nums_str = input("Enter numbers (Int/Float) separated by commas: ")
            nums = parse_numbers_input(nums_str)
            try:
                result = min_max(nums)
                print("(минимум, максимум):", result)
            except ValueError:
                print("ValueError")

        elif choice == "2":
            nums_str = input("Enter numbers (Int/Float) separated by commas: ")
            nums = parse_numbers_input(nums_str)
            result = unique_sorted(nums)
            print("unique_sorted_list:", result)

        elif choice == "3":
            matrix_str = input(
                "Enter full matrix (Python lists/tuples) e.g. [[1,2], (3,4)]: "
            )
            try:
                matrix = parse_matrix_input(matrix_str)
                print("Flattened list:", flatten(matrix))
            except (TypeError, ValueError) as e:
                print(e)

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
