import subprocess
# **************************Nodo Lista Simple...
class NodoLista():
    def __init__(self,dato,carne):
        self.dato=dato
        self.carne=carne
        self.sig=None

class Lista():
    def __init__(self):
        self.primero=None
        self.ultimo=None


    def vacia(self):
        return self.primero==None

    def AgregarLista(self,dato,carne):
        if(self.vacia()==True):
            self.primero=self.ultimo=NodoLista(dato,carne)

        else:
            aux = NodoLista(dato,carne)
            aux.sig = self.primero
            self.primero = aux


    def EliminarCola(self):
        aux = self.primero
        while(aux.sig != self.ultimo):
            aux = aux.sig
        print("salio>>",aux.sig.dato)
        aux2 = aux.sig.dato
        aux.sig = None
        self.ultimo = aux


    def MostrarLista(self):
        aux = self.primero
        print("************Mostrar Lista*************")
        while aux != None:
            print(aux.dato)
            aux=aux.sig

    def Modificar(self,ip,carne):
        aux = self.primero
        print("************Modificar Lista*************")
        while aux != None:
            if(aux.dato==ip):
                aux.carne=carne
            aux = aux.sig
        self.GragficarLista()

    def BuscarCarne(self,ip):
        aux = self.primero
        while aux != None:
            if (aux.dato == ip):
                carne = aux.carne
            aux = aux.sig
        return carne




    def GragficarLista(self):
        Archivo = open('C:/Users/Administrador/Desktop/Flask/Lista.dot', 'w')
        Grafo_dot = "digraph Lista{\nlabel = \"Lista\"\n\n"
        temp = self.primero

        Indice = 0
        while (temp != None):
            Grafo_dot += "\tNode" + str(Indice) + "[label = \"" + str(temp.dato) +"  ,  "+str(temp.carne)+ "\"];\n"
            temp = temp.sig
            Indice = Indice + 1
        Grafo_dot += "\n"
        temp = self.primero
        Indice = 0
        while (temp.sig != None):
            Grafo_dot += "\tNode" + str(Indice) + " -> Node" + str(Indice + 1) + ";\n"
            temp = temp.sig
            Indice = Indice + 1
        Grafo_dot += "}"
        Archivo.write(Grafo_dot)
        Archivo.close()
        subprocess.call(
            ['dot', 'C:/Users/Administrador/Desktop/Flask/Lista.dot', '-o',
             'C:/Users/Administrador/Desktop/Flask/Lista.png',
             '-Tpng', '-Gcharset=utf8'])


