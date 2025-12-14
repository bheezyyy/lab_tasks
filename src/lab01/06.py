s = input()
for i, c in enumerate(s):
    if c.isupper():
        start = i
        break
for j in range(start, len(s)):
    if s[j].isdigit():
        step = j - start + 1
        break
print(s[start::step])
