from zooAnimales.animal import Animal

class Zona:
    
    def __init__(self, nombre, zoo = None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales=[]

    def agregarAnimales(self,animal):
        self._animales.append(animal)

    def cantidadAnimales(self):
        x = 0
        
        for i in self._animales:
            x += 1
        return x 

    def getNombre(self):
        return self._nombre

    def setNombre(self,nombre):
        self,nombre=nombre

    def setZoo(self,zoo):
        self._zoo=zoo

    def getZoo(self):
        return self._zoo