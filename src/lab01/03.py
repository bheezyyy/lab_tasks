p = float(input().replace(',', '.'))  # preço
d = float(input().replace(',', '.'))  # desconto %
n = float(input().replace(',', '.'))  # imposto %

b = p * (1 - d/100)
tax = b * n / 100
total = b + tax

print(f'Base: {round(b, 2)} ₽')
print(f'Imposto: {round(tax, 2)} ₽')
print(f'Total: {round(total, 2)} ₽')
