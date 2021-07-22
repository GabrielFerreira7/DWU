import numpy as np
from individual import Individuo
import problem


def Tournament(frontNo):
    qnt = np.size(frontNo)
    MatingPool = list()

    for i in range(0, qnt):
        indice1 = np.random.randint(0, qnt)
        indice2 = np.random.randint(0, qnt)
        if frontNo[indice1] < frontNo[indice2]:
            MatingPool.append(indice1)
        else:
            MatingPool.append(indice2)

    return MatingPool


def Pmutation(Q, N):
    lim = 10
    u = np.random.uniform(0, 1)
    if u < 0.5:
        ptb = np.power((2*u), (1/(N+1)))
    else:
        ptb = 1 - (np.power((2*(1 - u)), (1/(N+1))))


    Q = Q + ptb*lim
    return Q


def sbx(MatingPool, PM):
    ob = MatingPool[0].getObj().shape[0]
    dim = MatingPool[0].getDec().shape[0]
    offspring = list()

    qnt = np.int(MatingPool.shape[0]/2)
    N = 20
    for i in range(0, qnt):
        u = np.random.uniform(0,1)
        if u <= 0.5:
            beta = np.power((2*u), (1/(N+1)))
        else:
            beta = np.power(1/2*(1-u), 1/(N+1))

        Q1 = 1/2*((1 + beta)*MatingPool[i].getDec() + (1 - beta)*MatingPool[i+qnt].getDec())
        Q2 = 1/2*((1 - beta)*MatingPool[i].getDec() + (1 + beta)*MatingPool[i+qnt].getDec())
        proM = np.random.uniform(0, 1)
        if proM < PM:
            Q1 = Pmutation(Q1, N)
            Q2 = Pmutation(Q2, N)
        #refletindo
        Q1 = -5 + np.abs((Q1 - (-5)))
        Q1 = 5 - np.abs(5 - Q1)
        Q2 = -5 + np.abs((Q2 - (-5)))
        Q2 = 5 - np.abs(5 - Q2)

        # transfomormado em individuo
        ind = Individuo(obj=ob, dec=dim)
        ind2 = Individuo(obj=ob, dec=dim)
        ind.setDec(Q1)
        ind2.setDec(Q2)
        ind.setObj(problem.problem1(Q1))
        ind2.setObj(problem.problem1(Q2))
        offspring.append(ind)
        offspring.append(ind2)

    return np.asarray(offspring)



