# ===== tuples.py =====

from typing import Tuple

# ===== Function =====


def format_record(rec: Tuple[str, str, float]) -> str:
    """
    Format a student record as a string.

    Args:
        rec: Tuple (fio: str, group: str, gpa: float)

    Returns:
        Formatted string: "Фамилия И.И., гр. GROUP, GPA 4.60"

    Raises:
        ValueError: if fio or group is empty.
        TypeError: if gpa is not a number.
    """
    if not isinstance(rec, tuple) or len(rec) != 3:
        raise TypeError("Record must be a tuple of (fio, group, gpa)")

    fio, group, gpa = rec

    # Validate
    if not fio.strip():
        raise ValueError("Full name cannot be empty")
    if not group.strip():
        raise ValueError("Group cannot be empty")
    if not isinstance(gpa, (float, int)):
        raise TypeError("GPA must be a number")

    # Normalize spaces
    parts = fio.strip().split()
    parts = [p.capitalize() for p in parts if p]  # capitalize first letter

    surname = parts[0]
    initials = ""
    for name in parts[1:3]:  # only first 2 names for initials
        initials += name[0].upper() + "."

    formatted = f"{surname} {initials}, гр. {group.strip()}, GPA {gpa:.2f}"
    return formatted


# ===== Interactive Menu =====


def main():
    print("=== Lab 02: Student Records ===")
    print("Enter student information to format it.")
    print("Type 'exit' at any prompt to quit.\n")

    while True:
        fio = input("Enter full name (Фамилия Имя [Отчество]): ").strip()
        if fio.lower() == "exit":
            break

        group = input("Enter group: ").strip()
        if group.lower() == "exit":
            break

        gpa_str = input("Enter GPA (float): ").strip()
        if gpa_str.lower() == "exit":
            break

        # Convert GPA
        try:
            gpa = float(gpa_str)
        except ValueError:
            print("GPA must be a number. Try again.\n")
            continue

        # Format record
        try:
            rec = (fio, group, gpa)
            formatted = format_record(rec)
            print("Formatted record:", formatted, "\n")
        except (ValueError, TypeError) as e:
            print("Error:", e, "\n")


if __name__ == "__main__":
    main()
