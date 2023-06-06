from zope.interface import implementer
from coleccionInterfaz import IColeccion
from claseNodo import Nodo

@implementer(IColeccion)
class Coleccion:
    __comiezo: Nodo
    
    def __init__(self):
        self.__comiezo = None
    
    def insertarElemento(self, objeto, posicion):
        if posicion == 0:
            aux = self.__comienzo
            self.__comienzo = objeto
            self.__comienzo.set_siguiente(aux)
        else:
            i = 0
            anterior = self.__comienzo
            posterior = self.__comienzo.get_siguiente()
            while i < posicion and posterior.get_siguiente() != None:
                anterior = posterior
                posterior = posterior.get_siguiente()
                i += 1
            if posterior == None:
                anterior.set_siguiente(objeto)
            else: 
                anterior.set_siguiente(objeto)
                objeto.set_siguiente(posterior)
        
    def agregarElemento(self, objeto):
        if self.__comienzo == None:
            self.__comienzo = objeto
        else:
            aux = self.__comienzo.get_siguiente()
            while aux.get_siguiente() != None:
                aux = aux.get_siguiente()
            aux.set_siguiente(objeto)

    def mostrarElemento(self, posicion):
        if posicion == 0:
            print(self.__comienzo)
        else:
            i = 0
            aux = self.__comienzo.get_siguiente()
            while i < posicion and aux.get_siguiente() != None:
                aux = aux.get_siguiente()
                i += 1
            print(aux)
