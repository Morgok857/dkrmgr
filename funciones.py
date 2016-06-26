#!/usr/bin/python3
import os
import subprocess

def run_command(command):
	#print(command)
	cmd = os.popen(command)
	return cmd
 
def dockerlist (sudo,hostt,ssh,hidden=""):
	oculto=""
	if hidden == True:
		oculto=" -a"
	if ssh == "127.0.0.1" or ssh == "localhost":
		comando=sudo +' docker ps '+oculto
	else:
		comando=ssh+' "'+sudo +' docker ps '+oculto+'"'
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
	if ssh == "127.0.0.1" or ssh == "localhost":
		comando=sudo+' docker ps '+oculto
	else:
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
		if host == "127.0.0.1" or host == "localhost":
			comando=sudo+' docker '+status+' '+container
		else:	
			comando=host+' "'+sudo+' docker '+status+' '+container+'"'
		#print(comando)
		run_command(comando)
		print()
		return True

	if status == "status":
		if host == "127.0.0.1" or host == "localhost":
			comadd2=sudo+' docker inspect --format="{{ .State.Running }}"'+' '+container
		else:
			comando=sudo+' docker inspect --format="{{ .State.Running }}"'+' '+container
			comadd2 = host+ " '" + comando  + "'"
		print('Status: ')
		os.system(comadd2)
		return True
	
	print(status+' no es un comando valido')
