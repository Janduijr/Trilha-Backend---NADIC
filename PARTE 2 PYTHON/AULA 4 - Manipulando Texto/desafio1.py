nome = input("DIGITE O SEU NOME COMPLETO: ")
espaco = nome.find(' ')


print(nome.upper()) #maisculo
print(nome.lower()) #minusculo
print(len(nome.replace(' ',''))) #numero de caracters sem espaco
print(nome[:espaco]) #primeiro nome

