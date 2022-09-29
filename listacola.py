from nodo import Nodo
class Queue():
    def __init__(self):
        self.primero = None
        self.rear=None
        self.size=0
        self.cola=[]
    def isEmpty(self):
        return self.primero == None
    def EnQueue(self, cliente):
        self.size+=1
        newNode = Nodo(dato=[cliente])
        if(self.primero):
            current = self.primero
            while(current.siguiente):
                current = current.siguiente
            current.siguiente = newNode
        else:
            self.primero = newNode
    def DeQueue(self):
        self.cola=[]
        self.size-=1
        temp = self.primero
        if (temp is not None):
            element = temp.dato
        self.primero= temp.siguiente
        temp = None
        return element
    def printlist(self):
        current = self.primero
        while(current):
            print(current.dato)
            self.cola.append(current.dato)
            current = current.siguiente
    def retcola(self):
        print("Cola",self.cola)
        return self.cola
   
    def delete(self):
        temp = self.primero
        if temp is None:
            print("\n No es posible limpiar el sistema")
        while temp:
            self.primero = temp.getsig()
            temp = None
            temp = self.primero
            self.size=0
   