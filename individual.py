import numpy as np
class Individuo:
    def __init__(self, obj, dec):
        self.obj = np.zeros(obj)
        self.dec = np.zeros(dec)
        self.nd = 0

    def setObj(self, valor):
        self.obj = valor

    def setDec(self, valor):
        self.dec = valor

    def getDec(self):
        return self.dec

    def getObj(self):
        return self.obj

