
import os
from xml.dom import minidom
from xml.etree.cElementTree import parse, Element
from tkinter import N, filedialog as fd
import numpy as np
from xml.dom import minidom
from listaempresas import listaempresas
lempresa=listaempresas()
a=""
while a !="7":
	print("-----MENU-----")
	print("1. Limpiar Sistema")
	print("2. Cargar Archivo Configuración del Sistema")
	print("3. Crear Nueva Empresa")
	print("4. Cargar Archivo con configuración Inicial para la prueba")
	print("5. Selección de empresa y punto de atención")
	print("6. Manejo de puntos de atención")
	print("7. Salir")
	a = input()
	if a=="1":
		clear = lambda: os.system('cls')
		clear()
		lempresa.delete()
		lempresa.printlist()
		
		
	if a=="2":
		clear = lambda: os.system('cls')
		clear()
		print("Cargar Archivo Configuración del Sistema")
		print("----------------------------------------------------------------------------------------------------------------------")
		filename = fd.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.xml*"),("all files", "*.*")))
		docxml=minidom.parse(filename)
		empresa = docxml.getElementsByTagName('empresa')
		nombre=docxml.getElementsByTagName('empresa')
		n=0
		for i in empresa:
			
			nombre=i.getElementsByTagName('nombre')
			abreviatura=i.getElementsByTagName('abreviatura')
			atencion=i.getElementsByTagName('puntoAtencion')
			transac=i.getElementsByTagName('transaccion')
			transaccion=i.getElementsByTagName('listaTransacciones')
			lid=(empresa[n].attributes['id'].value)
			n1=0
			atencionlist=[]
			for k in atencion:
				desktops=[]
				ateid=(atencion[n1].attributes['id'].value)
				nombreaten=k.getElementsByTagName('nombre')
				diraten=k.getElementsByTagName('direccion')
				escritorios=k.getElementsByTagName('escritorio')
				
			
				n2=0
				for j in escritorios:
					escritoriosid=(escritorios[n2].attributes['id'].value)
					escritoriosidentificacion=k.getElementsByTagName('identificacion')
					encargado=k.getElementsByTagName('encargado')
					desktops.append([escritoriosid,escritoriosidentificacion[n2].firstChild.data,encargado[n2].firstChild.data])
					n2+=1
				n1+=1
				atencionlist.append([ateid,nombreaten[0].firstChild.data,diraten[0].firstChild.data,desktops])
				print("Punto atención Empresa: ",n+1," ID ",ateid," Nombre: ",nombreaten[0].firstChild.data," Dirección: ",diraten[0].firstChild.data,"Escritorios: ",desktops)
				print("Escritorios punto de atención: ",n2, " empresa: ",n+1,desktops)
			
			n3=0
			transaccioneslist=[]
			for p in transac:
				transacid=(transac[n3-1].attributes['id'].value)
				nombretrac=p.getElementsByTagName('nombre')
				tiempo=p.getElementsByTagName('tiempoAtencion')
				transaccioneslist.append([transacid,nombretrac[n3-1].firstChild.data,tiempo[n3-1].firstChild.data])
				n3+=1
			lempresa.insertlast(lid,nombre[0].firstChild.data,abreviatura[0].firstChild.data,atencionlist,transaccioneslist)
			print("Transacciones empresa: ",n+1," ",transaccioneslist)
			n+=1
			print("----------------------------------------------------------------------------------------------------------------------")
		lempresa.printlist()
		
	if a=="3":
		clear = lambda: os.system('cls')
		clear()
		print(" Crear Nueva Empresa")
	if a=="4":
		clear = lambda: os.system('cls')
		clear()
		print("Cargar Archivo con configuración Inicial para la prueba")
		print("----------------------------------------------------------------------------------------------------------------------")
		filename2 = fd.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.xml*"),("all files", "*.*")))
		docxml2=minidom.parse(filename)
		
	if a=="5":
		clear = lambda: os.system('cls')
		clear()
		print("----------------------------------------------------------------------------------------------------------------------")
		print("Selección de empresa y punto de atención")
		print("Ingrese el ID de la empresa")
		empre=input()
		lempresa.getempresa(nombre=empre)
		lempresa.punto(nombre=empre)
	if a=="6":
		print("Manejo de puntos de atención")
	if a=="7":
		print("Salir")
		quit()