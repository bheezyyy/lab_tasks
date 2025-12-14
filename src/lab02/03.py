def name_to_initials(name):
    parts = name.strip().split()
    return (
        parts[0].capitalize() + " " + "".join([p[0].upper() + "." for p in parts[1:]])
    )


def format_student(data):
    name, grp, gpa = data
    if not name.strip():
        raise ValueError("Name empty")
    if not grp.strip():
        raise ValueError("Group empty")
    if not isinstance(gpa, float):
        raise TypeError("GPA type")

    print(f"{name_to_initials(name)}, group {grp}, GPA {gpa:.2f}")


format_student(("  petrova   anna  ivanovna ", "XYZ-01", 4.0))
