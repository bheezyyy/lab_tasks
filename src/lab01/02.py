a = input()
b = input()
a = float(a.replace(",", "."))
b = float(b.replace(",", "."))
avg = round((a + b) / 2, 2)
sumi = a + b
print(sumi, avg, sep="; ")
