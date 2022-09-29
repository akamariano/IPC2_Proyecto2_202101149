from nodo import Nodo
class listadesks():
    def __init__(self):
        self.primero=None
        self.ultimo = None
        self.size = 0
        self.construct=[]
    def insertlast(self,id,estado):
        # Mejor insertar al final
        
        newdesk= Nodo(dato=[id,estado])
        self.size += 1
        if self.primero is None:
            self.primero = newdesk
            self.ultimo = newdesk
        else:
            tmp = self.primero
            while tmp.getsig() is not None:
                tmp=tmp.getsig()
            tmp.setsig(newdesk)
    def printlist(self):
        print("---------------------------------------------------")
        print("Escritorios")
        tmp = self.primero
        # print("Empresas añadidas: ",self.size)
        while tmp is not None:
            print("Desk ID: ",tmp.dato[0],"Desk State: ",tmp.dato[1])
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
            self.construct.append([tmp.dato[0],tmp.dato[1]])
            tmp=tmp.getsig()    
    def returnclientes(self):
        return self.construct
    