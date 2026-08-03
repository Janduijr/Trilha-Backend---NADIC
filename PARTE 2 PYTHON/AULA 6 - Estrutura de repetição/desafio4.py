maiores = 0
menores = 0
for x in range(0,6):
    x = int(input(f'digite a idade da pessoa {x}: '))
    if x >= 18:
        maiores += 1
    else:
        menores +=1
print(f'maiores: {maiores}\nmenores: {menores}')