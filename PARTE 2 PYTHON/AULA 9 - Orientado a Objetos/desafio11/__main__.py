from classes011 import Mago, Guerreiro

g1 = Guerreiro('jandui', 2000)
m1 = Mago('pedro', 1500)
g1.atacar(m1,1000)
m1.curar(300)
m1.atacar(g1,500)