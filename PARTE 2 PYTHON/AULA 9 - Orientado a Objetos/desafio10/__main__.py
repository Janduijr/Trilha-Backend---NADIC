from classes010 import Drone, Caminhao, Moto

dist = 20
entrega = Moto(dist)
print(f'o frete de {type(entrega).__name__} por um distancia de {dist}km: {entrega.calc_frete()}')

