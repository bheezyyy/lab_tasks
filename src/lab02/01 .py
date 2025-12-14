def min_max(lst):
    if not lst:
        raise ValueError("Empty list")
    return min(lst), max(lst)


def uniq_sorted(lst):
    return sorted(set(lst))


def flat(matrix):
    out = []
    for row in matrix:
        if not isinstance(row, (list, tuple)):
            raise TypeError("Invalid row type")
        out += row
    return out


print(min_max([-3.1, 2]))
print(uniq_sorted([1.0, 1, 2.5, 2.5, 0]))
print(flat([[1], [], [2, 3]]))
