from zooAnimales.animal import Animal

class Anfibio(Animal):
    
    _listado=[]
    ranas=0
    salamandras=0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso

        Anfibio._listado.append(self)
        Animal.setTotalAnimales(Animal.getTotalAnimales()+1)

    @classmethod
    def setListado(cls,listado):
        cls._listado=listado
  
    def setColorPiel(self,pelaje):
        self._colorPiel=pelaje
  
    def setVenenoso(self,patas):
        self._venenoso=patas
    
    def getColorPiel(self):
        return self._colorPiel
    
    def getVenenoso(self):
        return self._venenoso
  
    @classmethod
    def cantidadAnfibios(cls):
        x=0
        for e in cls._listado:
            if (str(type(e).__name__)=="Anfibio"):
                x+=1
        return x
  
    @classmethod
    def crearRana(self,nombre,edad,genero):
        Anfibio.ranas+=1
        return Anfibio(nombre,edad,"selva",genero,"rojo",True)
  
    @classmethod
    def crearSalamandra(self,nombre,edad,genero):
        Anfibio.salamandras+=1
        return Anfibio(nombre,edad,"selva",genero,"negro y amarillo",False)  
  
    def Movimiento(self):
        return "saltar"
    
    def isVenenoso(self):
        return self._venenoso