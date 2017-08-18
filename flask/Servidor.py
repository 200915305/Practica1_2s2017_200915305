import reloader as reloader
from flask import Flask, request, Response
from xml.dom import minidom
import json
import os
import time
app = Flask("Practica1")

from Cola import Cola
cola=Cola()

from ListaSimple import Lista
lista = Lista()

from Pila import Pila
pilaP = Pila()

from PilaTemp import PilaTemp
pilaTemp = PilaTemp()

# Comando para Cambiar la IP.............
# print(os.system('netsh interface ip set address name="Conexión de red inalámbrica" source=static addr=192.168.10.1 mask=255.255.255.0 gateway=192.168.10.100 store=persistent'))
# print(os.system('ipconfig'))

letras=list('ABCDEFGHIJKLMNOPQRSTUVXYZ')
numeros=list('0123456789')
N=50
pila=[]
PilaTemp=[]
tope=-1

def Rellenar():
    if(tope==(N-1)):
        print ('>>>>')
        return True
    return False

def vacia():
    if(tope==-1):
        '>>>>'
        return True
    return False

def push(dato):
    if(Rellenar()!=True):
        global tope
        tope=tope+1
        pila.insert(tope,dato)

def pop():
    if(vacia()!=True):
        global tope
        aux=pila[tope]
        del pila[tope]
        tope=tope-1
        return aux
    else:
        return -9999

def InFijo(i,Cadena):
    if(Cadena[i]=='^'):
        prioridadop=4
        return prioridadop
    elif(Cadena[i]=='*'):
        prioridadop=2
        return prioridadop
    elif(Cadena[i]=='/'):
        prioridadop=2
        return prioridadop
    elif(Cadena[i]=='+'):
        prioridadop=1
        return prioridadop
    elif(Cadena[i]=='-'):
        prioridadop=1
        return prioridadop
    elif(Cadena[i]=='('):
        prioridadop=5
        return prioridadop

def Pilaa(pila):
    if(pila[tope]=='^'):
        prioridadpi=3
        return prioridadpi
    elif(pila[tope]=='*'):
        prioridadpi=2
        return prioridadpi
    elif(pila[tope]=='/'):
        prioridadpi=2
        return prioridadpi
    elif(pila[tope]=='+'):
        prioridadpi=1
        return prioridadpi
    elif(pila[tope]=='-'):
        prioridadpi=1
        return prioridadpi
    elif(pila[tope]=='('):
        prioridadpi=0
        return prioridadpi

def POSFIJO(Entrada):
    try:
        PilaTemp.clear()
        pila.clear()
        a=""
        Cadena=list(Entrada.upper())
        Cadena.pop()
        Cadena = Cadena[1:]
       # print(Cadena)
        for i in range(len(Cadena)):
            if(Cadena[i] in letras or Cadena[i] in numeros):
                PilaTemp.append(Cadena[i])
            elif(Cadena[i]!=')'):
                if (tope==-1):
                    push(Cadena[i])
                else:
                    if(InFijo(i,Cadena)<=Pilaa(pila)):
                        Cadena.append(pop())
                        push(Cadena[i])
                    elif(InFijo(i, Cadena)>Pilaa(pila)):
                        push(Cadena[i])
            elif(Cadena[i]==')'):
                while (pila[tope]!='('):
                    PilaTemp.append(pop())
                if(pila[tope]=='('):
                    pop()
                elif(tope!=-1):
                    PilaTemp.append(pop())
        while (tope>-1):
            PilaTemp.append(pop())
            a= ''.join(PilaTemp)
        print (a)
        return a
    except:
        print("Error en la convercion de Infijo a Posfijo")


def JSON(entrada):

    try:
         Archivo = open('C:/Users/Administrador/Desktop/entrada1.json', 'w')
         Archivo.write(entrada)
         Archivo.close()

    except ValueError:
        print("no se a podido guardar el JSON")


    try:
         with open('C:/Users/Administrador/Desktop/entrada1.json') as contenido:

             cursos = json.load(contenido)
             nodo = cursos['nodos']['nodo']
             local = cursos['nodos']['local']

             for n in nodo:
                 lista.AgregarLista(n.get('ip'), "carne")
                 print(n.get('ip'))

         lista.GragficarLista()
         return local


    except ValueError:
         print("no se a podido leer el JSON")




#JSON()
#POSFIJO("(((2+3)*4)-7)")


def Resultado(posfijo):
    Flujo_de_Pila=""
    num1=0
    num2=0
    suma=0;

    Cadena = list(posfijo.upper())
    for i in range(len(Cadena)):
        if(Cadena[i]== '+'):
            Flujo_de_Pila = Flujo_de_Pila + "push(+)" + "\n"
            Flujo_de_Pila = Flujo_de_Pila + "pop(+)" + "\n"
            num1 =  pilaP.EliminarPrimero()
            Flujo_de_Pila=Flujo_de_Pila+"pop("+str(num1)+")"+"\n"
            num2 = pilaP.EliminarPrimero()
            Flujo_de_Pila = Flujo_de_Pila + "pop(" + str(num2) + ")" + "\n"
            suma = int(num2)+int(num1)
            Flujo_de_Pila = Flujo_de_Pila + "push(" + str(suma) + ")" + "\n"
            pilaP.AgreparPila(suma)
        elif(Cadena[i]== '-'):
            Flujo_de_Pila = Flujo_de_Pila + "push(-)" + "\n"
            Flujo_de_Pila = Flujo_de_Pila + "pop(-)" + "\n"
            num1 = pilaP.EliminarPrimero()
            Flujo_de_Pila = Flujo_de_Pila + "pop(" + str(num1) + ")" + "\n"
            num2 = pilaP.EliminarPrimero()
            Flujo_de_Pila = Flujo_de_Pila + "pop(" + str(num2) + ")" + "\n"

            suma = int(num2) - int(num1)
            Flujo_de_Pila = Flujo_de_Pila + "push(" + str(suma) + ")" + "\n"
            pilaP.AgreparPila(suma)
        elif(Cadena[i]== '*'):
            Flujo_de_Pila = Flujo_de_Pila + "push(*)" + "\n"
            Flujo_de_Pila = Flujo_de_Pila + "pop(*)" + "\n"
            num1 = pilaP.EliminarPrimero()
            Flujo_de_Pila = Flujo_de_Pila + "pop(" + str(num1) + ")" + "\n"
            num2 = pilaP.EliminarPrimero()
            Flujo_de_Pila = Flujo_de_Pila + "pop(" + str(num2) + ")" + "\n"

            suma = int(num2) * int(num1)
            Flujo_de_Pila = Flujo_de_Pila + "push(" + str(suma) + ")" + "\n"
            pilaP.AgreparPila(suma)
        else:
            Flujo_de_Pila = Flujo_de_Pila + "push(" + Cadena[i] + ")" + "\n"
            pilaP.AgreparPila(Cadena[i])

    #print(suma)
    #print(Flujo_de_Pila)

    return str(suma)+","+Flujo_de_Pila


#Resultado("23+1-")
Resultado("28+7*761+*+")



def ModificarIP(ip):
    print(os.system('netsh interface ip set address name="Conexión de red inalámbrica" source=static addr='+ip+' mask=255.255.255.0 gateway=192.168.0.1 store=persistent'))

def ModificarServidor(ip):
    time.sleep(5)
    print("Cambiar")
    app.run(debug=False,host=ip, port=5000)
    app.run(host=ip, port=5000,  debug=True)


@app.route('/JSON', methods=['POST'])
def AgregarLista():
    parametro = str(request.form['dato'])
    print("POST>>"+parametro)
    local = JSON(parametro)
    print("ip local..."+local)
    ModificarIP(local)
    ModificarServidor(local)
    return local

@app.route('/carne', methods=['POST'])
def Carne():
    try:
        parametro = str(request.form['carne'])
        parametro=parametro.split("*")
        print("ip>>" + parametro[0])
        print("carne>>" + parametro[1])
        lista.Modificar(parametro[0],parametro[1])
        return "OK"
    except ValueError:
         print("Error en el Metodo Carne")




@app.route('/mensaje', methods=['POST'])
def Mensajes():
    parametro = str(request.form['mensaje'])
    mensaje = parametro.replace("#","+")
    mensaje = mensaje.replace(" ", "")
    mensaje = mensaje.replace("\n", "")
    a = str(mensaje)
    print(mensaje)
    posfijo = POSFIJO(a)
    ip = request.remote_addr

    cola.AgregarCola(mensaje,ip,posfijo)
    cola.GragficarCola()



    return "200915305"

@app.route('/respuesta', methods=['POST'])
def Operar():
    parametro = str(request.form['respuesta'])

    operacion = cola.EliminarCola()
    print("POST>>" + operacion)
    ip = str(operacion)
    ip= ip.split(",")
    nip = lista.BuscarCarne(ip[1])
    print(".................s..............."+ip[2])
    infijo= Resultado(ip[2])

    return operacion+","+nip+","+infijo




@app.route('/conectado', methods=['GET'])
def MetodGet():
    print("GET>>")
    print(request.remote_addr)

   # cola.AgregarIP(ip)
    return "200915305"


@app.route("/")
def hellof():
    print("...........vacio.........")
    return "***Servidor Flask y Python***"


if __name__ == "__main__":

     app.run(host='127.0.0.1', port=5000,  debug=True)

    # app.run(host='127.0.0.2', port=5000, debug=True)
