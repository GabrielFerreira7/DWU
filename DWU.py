import numpy as np
import NDSort


def infoDominance(pop):
    N = np.size(pop)
    D = np.zeros((N,N))
    for i in range(0, N-1):
        for j in range(i+1, N):
            k = np.int(np.any((pop[i].obj < pop[j].obj))) - np.int(np.any((pop[i].obj >pop[j].obj)))
            if k == 1:
                D[i,j] = 1
            elif k == -1:
                D[j,i] = 1

    cn = np.sum(D,1)
    return np.sum(D*cn,1)



def WD(pop, infoD, i, j): # calculo da distancia WD
    if i == j:
        wdij = 0
    else:
        wdij = np.sqrt(np.sum(np.power((pop[i].getDec() - pop[j].getDec()), 2)))
        wdij = wdij / (np.abs((infoD[i] - infoD[j])) + 1)

    return wdij


def dwu(pop, K): # DWU heuristc
    '''

    :param pop: população concatenada
    :param K: Tamanho da população original
    :return: próxima geração de tamanho K
    '''
    infoD = infoDominance(pop)
    Next = np.arange(K)*-1
    #frontNO = NDSort.front(pop)
    cont = 1
    WDs = np.zeros((pop.shape[0], pop.shape[0])) -1 #guarda os valores de WD
    menor = np.zeros(2) -1
    maior = np.zeros(2) - 1
    Nd = np.zeros(3)*-1 # variavel auxiliar que guarda 2 indices de inviduos e sua respectiva distância WD
    Nd2 = np.zeros(3)*-1

    #ver = np.where(frontNO == 1)
    #ver = np.reshape(ver, np.size(ver))
    ver = NDSort.front2(pop) # indice dos individuos não dominados


    if np.size(ver) == 1: # apenas um individuo não dominado
        Next[0] = int(ver[0])

    else: # mais de um indivduo não dominado,
        cont =2
        for i in range(0, (np.size(ver) - 1)):
            Nd[0] = ver[i] # individuo inicial a ser adotado
            Nd[1] = ver[i+1]

            if WDs[ver[i]][ver[i+1]] == -1: # distância WD dos individuos I e I +1 não calculado
                WDs[ver[i]][ver[i + 1]] = WD(pop, infoD, i, i+1)
            Nd[2] = WDs[ver[i]][ver[i+1]] #
            for j in range(i+1, np.size(ver)):
                if WDs[ver[i]][ver[j]] == -1: # distância WD dos individuos I e J não calculado
                    WDs[ver[i]][ver[j]] = WD(pop, infoD, i, j)

                if(Nd[2] < WDs[ver[i]][ver[j]]):
                    Nd[0] = ver[i]
                    Nd[1] = ver[j]
                    Nd[2] = WDs[ver[i]][ver[j]]
            if(Nd2[2] < Nd[2]):
                Nd2 = np.copy(Nd) # individuos que "até então", serão adicionados a população

        Next[0] = Nd2[0]
        Next[1] = Nd2[1]
# fim da seleção dos indivudos não dominados

    while(cont < K):
        for i in range(0, pop.shape[0]):
            ver = np.where(Next == i) # verifica se o individuo na posição i, já esta selecionado(está em Next)
            if np.size(ver) == 0:
                for j in range(0, cont): # compara os que ja foram selecionados
                    if WDs[i][j] == -1:
                        WDs[i][j] = WD(pop, infoD, i, j)

                    if menor[1] > WDs[i][j] or menor[1] == -1 :
                        # if com o objetivo de guardar a menor distancia de um individuo i com...
                        # os que já foram selecionados
                        menor[0] = i
                        menor[1] = WDs[i][j]

            if maior[1] < menor[1]: # guardar o individuo, em que a distância WD minima, seja a maior possível
                maior = np.copy(menor)
            menor[1] = -1

        Next[cont] = np.copy(maior[0])
        maior[1] = -1
        cont = cont + 1
    #Next = np.sort(Next)

    return pop[Next]