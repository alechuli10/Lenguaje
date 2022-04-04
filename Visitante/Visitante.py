class Visitante:
  def visitBloque (self,bloque):
    resultado= ""
    for instruccion in bloque.instrucciones:
      resultado+= instruccion.acepta(self)+"\n"
    return resultado
      
  def visitMientrasQue (self,mientrasQue):
    resultado= "while "+ mientrasQue.condicion+ ":\n"
    resultado+= mientrasQue.bloque.acepta(self)+"\n"
    return resultado
    
  def visitMostrar (self,mostrar):
    resultado= "print("+ mostrar.mensaje+ ")"
    return resultado
    
  def visitSi (sef,si):
    resultado= "if "+ si.condicion+ ":\n"
    resultado+= si.entonces+ "\n"
    resultado+= "else:\n"
    resultado+= si.si_no + "\n"
    return resultado