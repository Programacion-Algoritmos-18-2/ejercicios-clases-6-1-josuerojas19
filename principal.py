#importacion de las clases
from MiArchivo.miarchivo import Miarchivo
from Mimodelo.miModelo import Busqueda

m = Miarchivo("datos.txt")#creacion de objeto de tipo Miarchivo para abrir el archivo

lista = m.obtener_informacion()#lista que recibe la informacion del archivo
lista = [l.split(",") for l in lista]
n_list = []
#Ciclos for que recorren la lista de elmentos
for g in lista:
    for d in g:
        aux = int(d)
        n_list.append(aux)

m.cerrar_archivo()
n_list.sort(key=int)#ordena la lista
print(n_list)#imprime la lista ordenada
buscar = Busqueda(n_list)#creacion de objeto de tipo Busqueda que se le envia la lista
elemento = input("Ingrese elemento a buscar: ")#se pide al usuario que ingrese el elemento a buscar
print("El elemento ", elemento, " se encuentra en la posicion: ", buscar.busqueda_binaria(int(elemento)))





