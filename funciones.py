#!/usr/bin/python3
import os
import subprocess

def showhelp (pathhelp):
	try:
		path=pathhelp+'/help.ini'
		fopen=open(path,'r')
		for h in fopen:
			print(h)
		fopen.close()
	except Exception as e:
		print(" No se puede cargar la Ayuda") 

def run_command(command):
	cmd = os.popen(command)
	return cmd
 
def dockerlist (sudo,hostt,ssh,hidden=""):
	oculto=""
	if hidden == True:
		oculto=" -a"
	comando=ssh+' "'+sudo +' docker ps '+oculto+'"'
	#print(comando)
	list = run_command(comando)
	for lista in list:
		t = lista.split()
		if t[0] == 'CONTAINER':
			pass
		else:
			sinn = lista.split('\n')
			print(sinn[0] + "\t\t" + hostt)

def dockersearch (sudo,host,ssh,string,hidden=""):
	oculto=""
	if hidden == True:
		oculto=" -a"
	comando=ssh+' "'+sudo+' docker ps '+oculto+'"'
	list = run_command(comando)
	for lista in list:
		t = lista.split()
		if t[0] == 'CONTAINER':
			pass
		if lista.find(string) != -1:
			sinn = lista.split('\n')
			print(sinn[0]+ "\t\t" + host)
			
def dockerstat (sudo,host,container,status):
	if status == "start" or status == "stop":	
		comando=host+' "'+sudo+' docker '+status+' '+container+'"'
		#print(comando)
		run_command(comando)
		print()
		print("Puede demorar un poco en iniciar/detener el contenedor")
	else:
		print(status+' no es un comando valido')
