
import os
from xml.dom import minidom
from xml.etree.cElementTree import parse, Element
from tkinter import N, filedialog as fd
import numpy as np
from xml.dom import minidom
from listaempresas import listaempresas
from listasimulacion import listasimulacion
from listacola import Queue
from listaclientes import listaclientes
from escitoriossim import listadesks
import graphviz as gp
from tkinter import messagebox

lempresa=listaempresas()
lsimul=listasimulacion()
lcola=Queue()
lclientes=listaclientes()
ldesk=listadesks()
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
		docxml2=minidom.parse(filename2)
		print(docxml2)
		config=docxml2.getElementsByTagName('configInicial')
		idconfig=(config[0].attributes['id'].value)
		idempresa=(config[0].attributes['idEmpresa'].value)
		idpunto=(config[0].attributes['idPunto'].value)
		print("ID Configuración: ",idconfig," ID Empresa: ",idempresa," ID Punto: ", idpunto)
		lempresa.getempresa(nombre=idempresa)
		lempresa.puntodoc2(nombre=idempresa,p=idpunto)
		escritorioprueba=docxml2.getElementsByTagName('escritorio')
		cont=0
		deskactivos=[]
		for e in escritorioprueba:
			idpruebadesk=(escritorioprueba[cont].attributes['idEscritorio'].value)
			deskactivos.append(idpruebadesk)
			cont+=1
		cliente=docxml2.getElementsByTagName('cliente')
		cont1=0
		clientes=[]
		for c in cliente:
			idcliente=(cliente[cont1].attributes['dpi'].value)
			nombreclient=c.getElementsByTagName('nombre')
			transacclient=c.getElementsByTagName('transaccion')
			cont2=0
			transaccionesclientes=[]
			for t in transacclient:
				idtransacclient=(transacclient[cont2].attributes['idTransaccion'].value)
				cantidadtransacclient=(transacclient[cont2].attributes['cantidad'].value)
				transaccionesclientes.append([idtransacclient,cantidadtransacclient])
				cont2+=1
			# clientes.append([idcliente,nombreclient[0].firstChild.data,transaccionesclientes])
			lclientes.insertlast(idcliente,nombreclient[0].firstChild.data,transaccionesclientes)
			cont1+=1

		print("Escritorios activos: ", deskactivos)
		#
		
		#

		# Z = gp.Digraph(filename = 'prueba.gv')
		# Z.attr(rankdir='LR')
		# Z.attr('node', margin=0, fontcolor='blue', fontsize=14 ,height=2, width=2 ,shape='box', style='filled')
		# Z.attr('edge', arrowhead='vee', arrowtail='inv', color='green', fontcolor='blue')
		# for dib in deskactivos:
		# 	Z.node(dib)
		lclientes.printlist()
		lempresa.desksa(nombre=idempresa,p=idpunto)
		d=lempresa.getdesk()
		lsimul.insertlast(idempresa,idpunto,d,deskactivos,clientes)
		# print("CLIENTEEEEEEES",clientes)
		lclientes.clientesget()
		clientes = lclientes.returnclientes()
		

		n=0
		for cli in clientes:
			n+=1
			print(n,cli)
			lcola.EnQueue(cli)

		for ii in d:
				if ii[0] not in deskactivos:
					ldesk.insertlast(ii,"INACTIVO")
				else:
					ldesk.insertlast(ii,"ACTIVO")
		ldesk.clientesget()
		deskprueba=ldesk.returnclientes()
		
		print("ESTADO ESCRITORIOS")
		
		ldesk.printlist()
		contad=0
		print("Estado 0")
		lcola.printlist()
		f = gp.Digraph(filename = "digram2.gv")
		for cc in clientes:
			f.node_attr['shape'] = 'box'
			f.node_attr['peripheries'] = '3'
			f.graph_attr['rankdir'] = 'RL'
			f.node_attr['style'] = 'filled'
			# f.node_attr['fillcolor'] = 'lightblue'
			f.node(str(cc))
		conted=0
		for dd in deskprueba:
			print(dd)
			print(deskprueba[conted][1])
			f.node("ESCRITORIO"+str(dd))
			f.node_attr['shape'] = 'box'
			f.node_attr['peripheries'] = '3'
			f.graph_attr['rankdir'] = 'RL'
			f.node_attr['style'] = 'filled'
			f.node_attr['fillcolor'] = '#FFA63B'
			
			conted+=1
		f.render(filename='IPC2_Proyecto2_202101149/Cola/Estado0', format="png",view=0, cleanup=1)
		# lcola.coladigraph()
		# cola=lcola.retcola()
		# p = gp.Digraph(filename = "digram10.gv")
		# for nn in cola:
		# 	p.node(str(nn))
		# p.render(filename='Estados/Estado0Cola', format="png",view=0, cleanup=1)

		modif=""
		conteoname=0
		histo=[]
		while lcola.size !=0:
			contad+=1
			print(" ¿Desea Modificar activar/desactivar escritorios? S/N")
			modif=input()
			if modif == "S":
					print("Ingrese el número de escritorio")
					numdesk=input()
					for ddd in range (len(deskprueba)):
						# print(deskprueba[ddd][0][0])
						if str(deskprueba[ddd][0][0])==str(numdesk):
							print("ingrese el estado del escritorio")
							state=input()
							deskprueba[ddd][1]=state
							break
			f = gp.Digraph(filename = "digram2.gv")
			for jj in range (len(deskprueba)):
				
							# print(deskprueba[ddd][1])
							# print("ESTADO",state)
				#Verifico estado de escritorios
				# print(deskprueba[jj][1])
				if deskprueba[jj][1]=="ACTIVO" and deskprueba[jj][1]!="ATENDIENDO" and lcola.size!=0:
					conteoname+=1
					print("Cliente"," siendo atendido en: ",deskprueba[jj][0])
					f.node_attr['shape'] = 'box'
					f.node_attr['peripheries'] = '3'
					f.graph_attr['rankdir'] = 'RL'
					f.node_attr['style'] = 'filled'
					f.node_attr['fillcolor'] = '#FFA63B'
					f.node("Atendiendo cliente en"+(str(deskprueba[jj][0])))
					
					# histo.append("Cliente"+" siendo atendido en: "+str(deskprueba[jj][0]))
					# f.node("ATENDIDO EN: "+str(deskprueba[jj][0]))
					
					deskprueba[jj][1]="ATENDIENDO"
					lcola.DeQueue()
					deskprueba[jj][1]="ACTIVO"

			print("Estado: ",contad)
			lcola.printlist()
			que=lcola.retcola()
			
			
			for q in que:
				f.node_attr['shape'] = 'box'
				f.node_attr['peripheries'] = '3'
				f.graph_attr['rankdir'] = 'RL'
				f.node_attr['style'] = 'filled'
				f.node_attr['fillcolor'] = '#FFA63B'
				f.node(str(q))
				
			f.render(filename='IPC2_Proyecto2_202101149/Cola/Estado'+str(contad), format="png",view=0, cleanup=1)


		if lcola.size==0:
			# f = gp.Digraph(filename = "digram2.gv")
			# newcola=lcola.retcola()
			# for pp in newcola:
			# 	f.node(str(pp))
			# f.render(filename='Pacientes/Paciente'+str(conteoname+1), format="png",view=0, cleanup=1)
			print("Cola terminada y vaciada")
			messagebox.showinfo(message="COLA VACÍA, SIMULACIÓN TERMINADA", title="COLA")
			print(lcola.size)

		# p = gp.Digraph(filename = "digram3.gv")
		# newcola=lcola.retcola()
		# for pp in newcola:
		# 	p.node(str(pp))
		# p.render(filename='Pacientes/Paciente'+str(conteoname+1), format="png",view=0, cleanup=1)

			



				
				

		# print("Cola")
		# lcola.printlist()
		# lcola.DeQueue()
		# print("Cola 2")
		# lcola.printlist()
		# print(lcola.size)
		# lcola.printlist()
		
		
		
		
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