list = []
maior = 0
maiori = []
menor = 0
menori = []
for x in range(0,5):
    list.append(int(input(f'digite o {x} numero: '))) 
    if x > 0:
        if list[x] > maior:
            maior = list[x]
            maiori = [x]
        elif list[x] == maior:
            maiori.append(x) 
        if list[x] < menor:
            menor = list[x]
            menori = [x]
        elif list[x] == menor:
            menori.append(x)
        
    else:
        maior = list[x]
        maiori = [x]
        menor = list[x]
        menori = [x]
    
            
print(f'o menor {menor} esta na posicao {menori}')
print(f'o maior {maior} esta na posicao {maiori}')
        


