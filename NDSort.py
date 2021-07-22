import numpy as np

def calc(Objs1, Objs2): # verifica se um idividuo domina o outro
    qnt = Objs1.shape[0] # quantidade de objetivos a serem analisados
    cont = 0
    cont2 = 0
    for i in range(0, qnt):
        if Objs1[i] < Objs2[i]:
            cont = cont + 1
        elif Objs1[i] > Objs2[i]:
            cont2 = cont2 + 1
        else:
            cont2 = cont2 + 1
            cont = cont + 1

    if cont == cont2:
        return 0 # nao ha dominancia
    elif cont == qnt:
        return 1 # primeiro individuo domina o segundo
    elif cont2 == qnt:
        return -1 # segundo individuo domina o primeiro
    else:
        return 0 # nao ha dominancia



def front(pop):
    '''
    :param pop: população de individuos
    :return: vetor [1,n] em que cada posição equivale a fronteira de um individuo
    '''
    tam = pop.shape[0]
    cont1 = 1
    front = np.zeros(tam)
    pop2 = list()   # guarda os indices dos individuos que ja possuem fronteira

    while np.size(pop2) !=tam: # controla cada nivel da fronteira, 1, 2... m
        D = list()
        ND = list()
        for i in range(0, tam):
            if not(i in D) and not(i in pop2): # verifica se o individuo não foi dominado em outra interação
                cont = 0                            # e se já não possui fronteira
                obj1 = pop[i].obj
                for j in range(0, tam):
                    if not(j in pop2): #verifica se o individuo do Indice J, não possui fornteira
                        obj2 = pop[j].obj
                        Dm = calc(obj1, obj2) # verificação da dominância
                        if Dm == 0: # não ha dominância
                            cont = cont + 1
                        elif Dm == 1:
                            cont = cont + 1
                            D.append(j) # individuo j é dominado
                if (cont + np.size(pop2)) == tam: # encontrou um não dominado
                    ND.append(i)
                    front[i] = cont1

        pop2 = pop2 + ND
        cont1 = cont1 + 1

    return front



def front2(pop): #retorna os indices dos individuos não dominados
    '''
    :param pop: população do tamanho 2N(populção da geração + filhos)
    :return: indices dos individuos não dominados
    '''
    tam = pop.shape[0]
    front = list()
    D = list() #Dominados

    for i in range(0, tam):
        obj1 = pop[i].obj
        cont = 0
        if not(i in D):
            j = i +1
            cont = i +1
            while(j<tam):
                obj2 = pop[j].obj
                Dm = calc(obj1, obj2)
                if Dm == 1: # primeiro individuo domina o segundo
                    D.append(j)
                    cont = cont + 1
                elif Dm == -1: #segundo individuo domina o primeiro
                    # se o individuo i é dominado, podemos encerrar a execução do laço mais interno
                    cont = 0
                    j = tam
                else: # não existe dominância
                    cont = cont +1

                j = j+1

        if cont == tam: #individuo não dominado
            front.append(i)


    return front