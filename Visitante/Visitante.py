class Visitante:
  def __init__ (self):
    self.nivel= 0
 
  def tabular (self):
    resultado= ""
    for i in range(self.nivel):
      resultado+= "\t"
    return resultado
 
  def visitBloque (self,bloque):
    resultado= ""
    for instruccion in bloque.instrucciones:
      resultado+= instruccion.acepta(self)+"\n"
    return resultado
     
  def visitMientrasQue (self,mientrasQue):
    resultado= self.tabular()+ "while "+ str(mientrasQue.condicion)+ ":\n"
    self.nivel+= 1
    resultado+= mientrasQue.bloque.acepta(self)+"\n"
    self.nivel-= 1
    return resultado
   
  def visitMostrar (self,mostrar):
    resultado= self.tabular()+ "print("+ mostrar.mensaje+ ")"
    return resultado
   
  def visitSi (self,si):
    resultado= self.tabular()+ "if "+ str(si.condicion)+ ":\n"
    self.nivel+= 1
    resultado+= si.entonces.acepta(self)+ "\n"
    self.nivel-= 1
    resultado+= self.tabular()+ "else:\n"
    self.nivel+= 1
    resultado+= si.si_no.acepta(self) + "\n"
    self.nivel-= 1
    return resultado