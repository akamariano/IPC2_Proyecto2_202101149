from nodo import Nodo
class listasimulacion():
    def __init__(self):
        self.primero=None
        self.ultimo = None
        self.size = 0
    def insertlast(self,empresa,puntoatencion,escritorios,escritoriosactivos,clientes):
        # Mejor insertar al final
        
        newsimul= Nodo(dato=[empresa,puntoatencion,escritorios,escritoriosactivos,clientes])
        self.size += 1
        if self.primero is None:
            self.primero = newsimul
            self.ultimo = newsimul
        else:
            tmp = self.primero
            while tmp.getsig() is not None:
                tmp=tmp.getsig()
            tmp.setsig(newsimul)
    def printlist(self):
        print("---------------------------------------------------")
        print("Simulacion")
        tmp = self.primero
        # print("Empresas añadidas: ",self.size)
        while tmp is not None:
            print("Empresa: ",tmp.dato[0],"Punto de Atención: ",tmp.dato[1],"Escritorios: ",tmp.dato[2],"escritorios Activos: ",tmp.dato[3],"Clientes: ",tmp.dato[4])
            tmp=tmp.getsig()
        
    def getempresa(self, nombre):
        tmp = self.primero
        for x in range(self.size):
            if tmp.dato[0]== nombre:
                print("Empresa: ",tmp.dato[0],"Punto de Atención: ",tmp.dato[1],"Escritorios: ",tmp.dato[2],"escritorios Activos: ",tmp.dato[3],"Clientes: ",tmp.dato[4]) 
                
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
            print("\n No es posible limpiar el sistema")
        while temp:
            self.primero = temp.getsig()
            temp = None
            temp = self.primero
            self.size=0
        
    
    