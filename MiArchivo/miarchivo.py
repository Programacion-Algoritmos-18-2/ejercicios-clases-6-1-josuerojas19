import codecs

#Clase Miarchivo
class Miarchivo:

    def __init__(self, a):

        self.nuevo = a
        self.archivo = codecs.open(self.nuevo, "r")#abre el archivo
    #metodo para leer la informacion del archivo
    def obtener_informacion(self):

        return self.archivo.readlines()
    #metodo que cierra el archivo
    def cerrar_archivo(self):
        self.archivo.close()


