#fatiamento
texto = input("DIGITE O SEU NOME COMPLETO: ")
print(texto[7:14])
print(texto[:7])
#analise
print(len(texto)) #quantos caracters
print(texto.count('a')) #quantas vezes o caracter aparece
print(texto.count('a',0,14)) #contagem com fatiamento
print(texto.find('ui')) #posicao onde comecou o padrao
print('jandui' in texto) #aparece na variavel?
print(texto.replace('junior','senna')) #substitui
print(texto.upper()) # maiusculo
print(texto.lower()) # minusculo 