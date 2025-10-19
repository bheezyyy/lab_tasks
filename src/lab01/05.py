s = input().strip()
init = ''.join([x[0] for x in s.split()])
print(init)
print(len(s.replace(' ', '')) + 2)