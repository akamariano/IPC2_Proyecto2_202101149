from nodo import Nodo
class listaclientes():
    def __init__(self):
        self.primero=None
        self.ultimo = None
        self.size = 0
        self.construct=[]
    def insertlast(self,idclient,nombreclient,transactionclient):
        # Mejor insertar al final
        
        newclient= Nodo(dato=[idclient,nombreclient,transactionclient])
        self.size += 1
        if self.primero is None:
            self.primero = newclient
            self.ultimo = newclient
        else:
            tmp = self.primero
            while tmp.getsig() is not None:
                tmp=tmp.getsig()
            tmp.setsig(newclient)
    def printlist(self):
        print("---------------------------------------------------")
        print("Clientes y sus transacciones")
        tmp = self.primero
        # print("Empresas añadidas: ",self.size)
        while tmp is not None:
            print("Cliente ID: ",tmp.dato[0],"Nombre CLiente: ",tmp.dato[1],"Transacciones Cliente: ",tmp.dato[2])
            tmp=tmp.getsig()
        

    def delete(self):
        temp = self.primero
        if temp is None:
            print("\n No es posible limpiar el sistema")
        while temp:
            self.primero = temp.getsig()
            temp = None
            temp = self.primero
            self.size=0
    def clientesget(self):
        tmp = self.primero
        while tmp is not None:
            self.construct.append([tmp.dato[0],tmp.dato[1],tmp.dato[2]])
            tmp=tmp.getsig()    
    def returnclientes(self):
        return self.construct
    