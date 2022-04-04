from Sintaxis.Visitable import Visitable


class Mostrar(Visitable): 
    # Una instrucción para mostrar un mensaje 
    # en salida estándar. 
    def __init__(self, mensaje): 
        self.mensaje = mensaje 