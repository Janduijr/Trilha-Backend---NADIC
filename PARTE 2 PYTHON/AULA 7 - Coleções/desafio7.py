nomes = []
galera = []
for x in range(0,3):
    nomes.append(input('digite um nome: '))
    nomes.append(int(input('digite a idade: ')))
    galera.append(nomes[:])
    nomes.clear()
for p in range(0,len(galera)):
    if galera[p][1] >= 18:
        print(f'{galera[p][0]} tem {galera[p][1]} anos')
        
