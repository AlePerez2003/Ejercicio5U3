class Nodo:
    __nodo: object
    __siguiente: object
    
    def __init__(self, objeto):
        self.__nodo = objeto
        self.__siguiente = None
        
    def set_siguiente(self, siguiente):
        self.__siguiente = siguiente
        
    def get_siguiente(self):
        return self.__siguiente
    
    def get_dato(self):
        return self.__nodo