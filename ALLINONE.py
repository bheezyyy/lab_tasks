def min_max(numbers):
    """Return the minimum and maximum values from a list of numbers."""
    return min(numbers), max(numbers)

def unique_sorted(numbers):
    """Return a sorted list of unique values from the input list."""
    return sorted(set(numbers))

def flatten(matrix):
    """Flatten a 2D matrix into a 1D list."""
    if not all(isinstance(row, (list, tuple)) for row in matrix):
        raise ValueError("Input must be a list of lists or tuples.")
    return [item for sublist in matrix for item in sublist]

def main():
    while True:
        print("\nSelect operation:")
        print("1 - min_max")
        print("2 - unique_sorted")
        print("3 - flatten (matrix)")
        print("0 - Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            try:
                numbers = list(map(float, input("Enter numbers (Int/Float) separated by commas: ").split(',')))
                result = min_max(numbers)
                print(f"(minimum, maximum): {result}")
            except ValueError:
                print("Invalid input. Please enter numbers separated by commas.")
        
        elif choice == '2':
            try:
                numbers = list(map(float, input("Enter numbers (Int/Float) separated by commas: ").split(',')))
                result = unique_sorted(numbers)
                print(f"unique_sorted_list: {result}")
            except ValueError:
                print("Invalid input. Please enter numbers separated by commas.")
        
        elif choice == '3':
            try:
                matrix_input = input("Enter a full matrix (Python lists/tuples) e.g. [[1,2], (3,4)]: ")
                matrix = eval(matrix_input)
                result = flatten(matrix)
                print(f"Flattened list: {result}")
            except ValueError as ve:
                print(ve)
            except Exception as e:
                print("Error: Please ensure you enter a valid matrix format.")
        
        elif choice == '0':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    main()
