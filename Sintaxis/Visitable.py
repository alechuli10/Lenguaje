class Visitable:
  def acepta (self,visitor):
    # Se recupera el nombre de la clase actual. 
        class_name = self.__class__.__name__ 
 
        # El método getattr() recuperará, en la instancia 
        # del visitante, el método cuyo nombre es 'visita' 
        # después el nombre de la clase. Si tal miembro no existe, 
        # se selecciona el método default(). 
        method = getattr(visitor, 'visit' + class_name)
 
        # Llamamos a este método con la instancia del visitable 
        # como parámetro. 
        return method(self)