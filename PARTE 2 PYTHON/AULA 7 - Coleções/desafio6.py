n = [[], []]

for x in range(0, 7):
    a = int(input(f'digite o {x} numero: '))
    
    if a % 2 == 0:
        if len(n[0]) == 0:
            n[0].append(a)
        else:
            pos = 0
            while pos < len(n[0]):
                if a < n[0][pos]:
                    n[0].insert(pos, a)
                    break
                else:
                    pos += 1
            else:
                n[0].append(a)
    else:
        if len(n[1]) == 0:
            n[1].append(a)
        else:
            pos = 0
            while pos < len(n[1]):
                if a < n[1][pos]:
                    n[1].insert(pos, a)
                    break
                else:
                    pos += 1
            else:
                n[1].append(a)

print(f'Pares: {n[0]}\nImpares: {n[1]}')