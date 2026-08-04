n = []
a = 0
for x in range(0,6):
    a = int(input(f'digite o {x} numero: '))
    if a in n:
        pass
    else:
        n.append(a)
print(sorted(n))