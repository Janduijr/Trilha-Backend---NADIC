n = []
a = 0
for x in range(0,5):
    a = int(input(f'digite o {x} numero: '))
    if x == 0 or a > n[-1]:
        n.append(a)
    else:
        pos = 0
        while pos < len(n):
            if a <= n[pos]:
                n.insert(pos, a)
                break
            pos += 1
print(n)
           
                