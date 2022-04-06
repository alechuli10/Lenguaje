from Visitante.Visitante import Visitante
from Sintaxis.Bloque import Bloque
from Sintaxis.MientrasQue import MientrasQue
from Sintaxis.Si import Si
from Sintaxis.Mostrar import Mostrar

def visitar ():
  mostrar_ok = Mostrar('"OK"') 
  mostrar_ko = Mostrar('"KO"') 
  alternativa = Si("2 + 2 == 4", mostrar_ok, mostrar_ko) 
  bloque_alternativa = Bloque() 
  bloque_alternativa.agregarInstruccion(alternativa) 
  bucle = MientrasQue(True, bloque_alternativa)
  visitante= Visitante()
  return bucle.acepta(visitante)