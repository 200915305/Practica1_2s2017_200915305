
import subprocess

class NodoCola():
    def __init__(self,dato,ip,pos):
        self.dato=dato
        self.ip=ip
        self.pos=pos
        self.sig=None

class Cola():
    def __init__(self):
        self.primero=None
        self.ultimo=None


    def vacia(self):
        return self.primero==None

    def AgregarCola(self,dato,ip,pos):
        if(self.vacia()==True):
            self.primero=self.ultimo=NodoCola(dato,ip,pos)

        else:
            aux = NodoCola(dato,ip,pos)
            aux.sig = self.primero
            self.primero = aux


    def EliminarCola(self):
        aux = self.primero
        while(aux.sig != self.ultimo):
            aux = aux.sig
        print("salio>>",aux.sig.dato)
        respuesta=aux.sig.dato+","+aux.sig.ip+","+aux.sig.pos
        aux2 = aux.sig.dato
        aux.sig = None
        self.ultimo = aux
        return respuesta


    def MostrarCola(self):
        aux = self.primero
        print("************Mostrar Cola*************")
        while aux != None:
            print(aux.dato)
            aux=aux.sig


    def GragficarCola(self):
        Archivo = open('C:/Users/Administrador/Desktop/Flask/Cola.dot', 'w')
        Grafo_dot = "digraph Cola{\nlabel = \"Cola\"\n\n"
        temp = self.primero

        Indice = 0
        while (temp != None):
            Grafo_dot += "\tNode" + str(Indice) + "[label = \"" +  str(temp.dato) +"  ,  "+str(temp.ip) +"  ,  "+str(temp.pos)+"\"];\n"
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
            ['dot', 'C:/Users/Administrador/Desktop/Flask/Cola.dot', '-o',
             'C:/Users/Administrador/Desktop/Flask/Cola.png',
             '-Tpng', '-Gcharset=utf8'])


cola = Cola()
"""""
cola.AgregarCola(1)
cola.AgregarCola(2)
cola.AgregarCola(3)
cola.AgregarCola(4)
cola.AgregarCola(5)
cola.AgregarCola(6)

cola.mostrarCola()
cola.GragficarCola()
cola.EliminarUltimo()
cola.GragficarCola()
cola.mostrarCola()
cola.EliminarUltimo()
cola.mostrarCola()
cola.EliminarUltimo()
cola.mostrarCola()
cola.EliminarUltimo()
cola.mostrarCola()
"""