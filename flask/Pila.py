import subprocess
# ************************************Nodo Pila....
class NodoPila():
    def __init__(self, dato):
        self.dato = dato
        self.sigP = None


# ************************************Pila....
class Pila():
    def __init__(self):
        self.primeroP = None
        self.ultimoP = None

    def vaciaP(self):
        return self.primeroP == None

    def AgreparPila(self, dato):
        if self.vaciaP() == True:
            self.primeroP = self.ultimoP = NodoPila(dato)
        else:
            aux = NodoPila(dato)
            aux.sigP = self.primeroP
            self.primeroP = aux

    def MostrarPila(self):
        aux = self.primeroP
        print ("************Mostrar Pila*************")
        while aux != None:
            print (aux.dato)
            aux = aux.sigP

    def EliminarPrimero(self):
        aux = self.primeroP
        self.primeroP = self.primeroP.sigP
        return aux.dato

    def GraficarPila(self):
        Archivo = open('C:/Users/Administrador/Desktop/Flask/Pila.dot', 'w')
        Grafo_dot = "digraph Pila{\nlabel = \"Pila\"\n\n"
        temp = self.primeroP

        Indice = 0
        while (temp != None):
            Grafo_dot += "\tNode" + str(Indice) + "[label = \"" + str(temp.dato) + "\"];\n"
            temp = temp.sigP
            Indice = Indice + 1
        Grafo_dot += "\n"
        temp = self.primeroP
        Indice = 0
        while (temp.sigP != None):
            Grafo_dot += "\tNode" + str(Indice) + " -> Node" + str(Indice + 1) + ";\n"
            temp = temp.sigP
            Indice = Indice + 1
        Grafo_dot += "}"
        Archivo.write(Grafo_dot)
        Archivo.close()
        subprocess.call(
            ['dot', 'C:/Users/Administrador/Desktop/Flask/Pila.dot', '-o','C:/Users/Administrador/Desktop/Flask/Pila.png',
             '-Tpng', '-Gcharset=utf8'])


pila = Pila()
"""""
pila.AgreparPila(1)
pila.AgreparPila(2)
pila.AgreparPila(3)
pila.AgreparPila(4)
pila.AgreparPila(5)
pila.AgreparPila(6)
pila.AgreparPila(7)
pila.AgreparPila(8)
pila.GraficarPila()
pila.MostrarPila()
pila.EliminarPrimero()
pila.MostrarPila()
"""