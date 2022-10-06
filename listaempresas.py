from nodo import Nodo
class listaempresas():
    def __init__(self):
        self.primero=None
        self.ultimo = None
        self.size = 0
        self.desks=[]
        self.times=""
    def insertlast(self,id,nombre,abrev,listaatencion,listatransac):
        # Mejor insertar al final
        
        newempresa= Nodo(dato=[id,nombre,abrev,listaatencion,listatransac])
        self.size += 1
        if self.primero is None:
            self.primero = newempresa
            self.ultimo = newempresa
        else:
            tmp = self.primero
            while tmp.getsig() is not None:
                tmp=tmp.getsig()
            tmp.setsig(newempresa)
    def printlist(self):
        print("---------------------------------------------------")
        print("Empresas y sus Atributos")
        tmp = self.primero
        print("Empresas añadidas: ",self.size)
        while tmp is not None:
            print("ID: ",tmp.dato[0],"Nombre: ",tmp.dato[1],"Abreviatura: ",tmp.dato[2],"Puntos de Atención: ",tmp.dato[3],"Transacciones: ",tmp.dato[4])
            tmp=tmp.getsig()
        
    def getempresa(self, nombre):
        tmp = self.primero
        for x in range(self.size):
            if tmp.dato[0]== nombre:
                print("ID: ",tmp.dato[0],"Nombre: ",tmp.dato[1],"Abreviatura: ",tmp.dato[2],"Puntos de Atención: ",tmp.dato[3],"Transacciones: ",tmp.dato[4]) 
                
                return tmp
            tmp = tmp.getsig()
    def puntodoc2(self, nombre,p):
        tmp = self.primero
        for x in range(self.size):
           
            if tmp.dato[0]== nombre:
                print("Puntos de Atención: ",tmp.dato[3])
                at=[]
                for x in tmp.dato[3]:
                    at.append(x)
                # print(at)
                # print("Seleccione su punto de atención")
                # p=input()
                n=0
                for x in at:
                    if at[n][0]==p:
                        print("Según el documento de configuración ha seleccionado: ",x)
                        
                    n+=1
                return tmp
            tmp = tmp.getsig()
    def punto(self, nombre):
        tmp = self.primero
        for x in range(self.size):
           
            if tmp.dato[0]== nombre:
                print("Puntos de Atención: ",tmp.dato[3])
                at=[]
                for x in tmp.dato[3]:
                    at.append(x)
                # print(at)
                print("Seleccione su punto de atención")
                p=input()
                n=0
                for x in at:
                    if at[n][0]==p:
                        print(x)
                        
                    n+=1
                return tmp
            tmp = tmp.getsig()
    def delete(self):
        temp = self.primero
        if temp is None:
            print("\n No es posible limpiar el sistema o no ha añadido empresas del tipo archivo de entrada 1")
        while temp:
            self.primero = temp.getsig()
            temp = None
            temp = self.primero
            self.size=0
    def desksa(self, nombre,p):
        tmp = self.primero
        for x in range(self.size):
           
            if tmp.dato[0]== nombre:
                # print("Puntos de Atención: ",tmp.dato[3])
                at=[]
                for x in tmp.dato[3]:
                    at.append(x)
                # print(at)
                # print("Seleccione su punto de atención")
                # p=input()
                n=0
                for x in at:
                    if at[n][0]==p:
                        print("Según el documento de configuración ha seleccionado: ",x)
                        print("Escritorios punto seleccionado: ",at[n][3])
                        cont=0
                        for a in at[n][3]:
                            cont+=1
                            self.desks.append(a)
                            print("Escritorio:",cont,a)
                        # self.desks=at[n][3]
                        
                    n+=1
                return tmp
            tmp = tmp.getsig()
    def getdesk(self):
        return self.desks
    def gettiempo(self,id):
        tmp = self.primero
        for x in range(self.size):
            if tmp.dato[0]== id:
                self.times=tmp.dato[4] 
                print("Transacciones de la empresa: ",tmp.dato[4])
                self.times=tmp.dato[4]
                print("Tiempo",self.times)
                return tmp
            tmp = tmp.getsig()

        
    
    