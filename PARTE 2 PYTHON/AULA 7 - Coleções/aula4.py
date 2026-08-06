p = {'nome': 'jandui', 'idade':21}
print(p['nome'])
p['sexo'] = 'M'
print(p.items())
print(p.keys())
print(p.values())
for k,v in p.items():
    print(f'o {k} e {v}!')