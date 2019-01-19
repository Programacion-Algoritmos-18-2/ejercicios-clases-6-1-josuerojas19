#calse Busqueda
class Busqueda(object):
    #Constructor de la calse que recibe un solo parametro
    def __init__(self, lista):
        self.lista = lista
        self.inferior = 0
        self.superior = len(self.lista)-1
        self.medio = int((self.inferior + self.superior + 1)/2)
        self.ubicacion = -1

    def agregar_lista(self, lista):
        self.lista = lista

    def obtener_lista(self):
        return self.lista

    #adaptacion del metodo de busqueda binaria que retorna la ubicacion del elemento a buscar
    def busqueda_binaria(self, elem):

        while self.inferior <= self.superior and self.ubicacion == -1:
            if elem == self.lista[self.medio]:
                self.ubicacion = self.medio
            elif elem < self.lista[self.medio]:
                self.superior = self.medio - 1
            else:
                self.inferior = self.medio + 1

            self.medio = int((self.inferior + self.superior + 1)/2)

        return self.ubicacion


