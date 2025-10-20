def transpose(m):
    if not m: return []
    if any(len(row) != len(m[0]) for row in m): raise ValueError("Jagged")
    return [list(x) for x in zip(*m)]

def row_sum(m):
    return [sum(r) for r in m]

def col_sum(m):
    if not m: return []
    if any(len(r) != len(m[0]) for r in m): raise ValueError("Jagged")
    return [sum(r[i] for r in m) for i in range(len(m[0]))]

print(transpose([[1,2],[3,4]]))
print(row_sum([[1,2,3],[4,5,6]]))
print(col_sum([[-1,1],[10,-10]]))