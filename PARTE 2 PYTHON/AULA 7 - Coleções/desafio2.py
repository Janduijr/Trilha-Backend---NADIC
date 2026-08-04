times = ('Palmeiras','Flamengo','Athletico-PR','Fluminense','Bahia','Bragantino','Cruzeiro','Botafogo','Corinthians','Atlético-MG')
print(times[0:4])
print(times[6:])
time = sorted(times)
print(time)
for x in range(0,len(times)):
    if times[x] == 'Corinthians':
        print(f'corinthias esta na posicao {x+1} da tabela')

        
