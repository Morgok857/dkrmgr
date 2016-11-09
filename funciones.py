#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import subprocess
from settings import *

def show_debug(showprint):
	if debug == "yes":
		print(showprint)

def run_command(command):
	show_debug(command)
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
		command_default=sudo+' docker '+status+' '+container
		if host == "127.0.0.1" or host == "localhost":
			comando=command_default
		else:	
			comando=host+' "'+command_default+'"'
		#print(comando)
		run_command(comando)
		print()
		return True

	if status == "status":
		comando=sudo+' docker inspect --format="{{ .State.Running }}"'+' '+container
		if host == "127.0.0.1" or host == "localhost":
			comadd2=comando
		else:
			comadd2 = host+ " '" + comando  + "'"
		print('Status: ')
		os.system(comadd2)
		return True
		
	if status == "ports":
		commando=sudo+' docker inspect --format="{{ .NetworkSettings.Ports }}"'+' '+container
		if host == "127.0.0.1" or host == "localhost":
			comadd2=comando
		else:
			comadd2 = host+ " '" + commando  + "'"
		portss=run_command(comadd2)
		result=portss.__next__()
		result=result.split("map")
		result=result[1]
		print(result)
		return True

	if status == "internalip":
		commando=sudo+' docker inspect --format="{{ .NetworkSettings.IPAddress }}"'+' '+container
		if host == "127.0.0.1" or host == "localhost":
			comadd2=comando
		else:
			comadd2 = host+ " '" + commando  + "'"
		result=run_command(comadd2)
		print("Ip: "+result.__next__())
		return True

	if status == "env":
                commando=sudo + ' docker inspect --format="{{ .Config.Env }}"' + ' ' + container
                if host == "127.0.0.1" or host == "localhost":
                        comadd2=commando
                else:
                        comadd2 = host+ " '" + commando  + "'"
                result=run_command(comadd2)
                print(result.__next__())
                return True

	print(status+' no es un comando valido')
