from Sintaxis.Visitable import Visitable

class Bloque(Visitable): 
    # Un bloque es un conjunto de instrucciones ejecutadas 
    # unas detrás de otras. 
    def __init__(self): 
        # Por defecto, un bloque no contiene ninguna instrucción. 
        self.instrucciones = [] 
 
    def agregarInstruccion(self, instruccion): 
        self.instrucciones.append(instruccion)