class Nodo():
	def __init__(self,dato):
		self.dato=dato
		self.siguiente = None
	def getsig(self):
		return self.siguiente
	def setsig(self, siguiente):
		self.siguiente= siguiente
    