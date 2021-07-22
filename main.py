import numpy as np
from individual import Individuo
import problem
import NDSort
import DWU
import GA
import matplotlib.pyplot as plt

def populacao_inicial(tam, dim, ob):
    pop = list()
    for i in range(0, tam):
        ind = Individuo(obj=ob, dec=dim)
        dec = np.random.uniform(-5,5, (dim))
        vp = problem.problem1(dec)
        ind.setDec(dec)
        ind.setObj(vp)
        pop.insert(i, ind)

    return np.asarray(pop)

def plot2(pop, ob):
    if ob == 2:
        ax.clear()
        plt.ylim(-5, 5)
        plt.xlim(-5, 5)
        vetorX1 = []
        vetorX2 = []
        for i in range(0, np.size(pop)):
            aux = pop[i].getObj()
            vetorX1.append(np.copy(aux[0]))
            vetorX2.append(np.copy(aux[1]))

        ax.scatter(vetorX1, vetorX2, s=40, c ='b', alpha=0.8)
        ax.set_xlabel("f1(x)")
        ax.set_ylabel("f2(x)")
        plt.pause(.01)


ob = 2 #objetivos
var = 2 # variaveis de decisao
n = 10 # quantidade de individuos
geracoes = 100
pop = populacao_inicial(n, var, ob)
cont = 0
PM = 0.3
if ob ==2:
    fig, ax = plt.subplots()
if ob == 3:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

while(cont<geracoes):


    frontNo = NDSort.front(pop)
    MatingPool = GA.Tournament(frontNo)
    Offspring = GA.sbx(pop[MatingPool], PM)
    pop = DWU.dwu(np.concatenate((pop, Offspring), axis=0), n)
    cont = cont + 1
    if cont%10 == 0:
        plot2(pop, ob)

plt.show()







