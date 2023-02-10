# Tenemos la clase Nodo1

class Nodo1:
    def __init__(self, dato):
        self.dato = dato
        self.sigt = None

#Tenemos la clase ListaEnlazadaCircular
class ListaEnlazadaCircular:
    # constructor
    def __init__(self):
        self.cabeza = None

    # creamos la funcion agregarUltimo
    def agregarUltimo(self, dato):
        nuevoNodo = Nodo1(dato)
        if self.cabeza is None:
            self.cabeza = nuevoNodo
            nuevoNodo.sigte = self.cabeza
        else:
            temp = self.cabeza
            while temp.igte != self.cabeza:
                temp = temp.sigte
            temp.sigte = nuevoNodo
            nuevoNodo.sigte = self.cabeza

    #Creamos la funcion eliminarUltimo
    def eliminarUltimo(self):
        if self.cabeza is None:
            return "La lista está vacía"
        elif self.cabeza.sigte == self.cabeza:
            temp = self.cabeza
            self.cabeza = None
            return str(temp.dato) + 'el dato fue eliminado de la lista'  
        else:
            temp = self.cabeza
            while temp.sigte.sigte != self.cabeza:
                temp = temp.sigte
            temp2 = temp.sigte
            temp.sigte = self.cabeza
            return str(temp2.dato) + 'el dato fue eliminado de la lista' 
        
    # Creamos la funcion agregarPrimero
    def agregarPrimero(self, dato):
        nuevoNodo = Nodo1(dato)
        temp = self.cabeza
        nuevoNodo.sigte = self.cabeza
        if self.cabeza is not None:
            while temp.sigte != self.cabeza:
                temp = temp.sigte
            temp.sigte = nuevoNodo
        else:
            nuevoNodo.sigte = nuevoNodo
        self.cabeza = nuevoNodo

    # Creamos la funcon eliminarPrimero
    def eliminarPrimero(self):
        if self.cabeza is None:
            return 'lista vacía' 
        elif self.cabeza.sigte == self.cabeza:
            temp = self.cabeza
            self.cabeza = None
            return str(temp.dato) + 'el dato fue eliminado de la lista' 
        else:
            temp = self.cabeza
            while temp.sigte != self.cabeza:
                temp = temp.sigte
            temp2 = self.cabeza
            self.cabeza = self.cabeza.sigte
            temp.sigte = self.cabeza
            return str(temp2.dato) + 'el dato fue eliminado de la lista' 

    # Creamos la funcion mostrarLista
    def mostrarLista(self):
        if self.cabeza is None:
            return 'lista vacía' 
        else:
            temp = self.cabeza
            lista = []
            while temp.sigte != self.cabeza:
                lista.append(temp.dato)
                temp = temp.sigte
            lista.append(temp.dato)
            return lista
