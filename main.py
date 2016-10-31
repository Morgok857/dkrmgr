#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys,os
import funciones
from settings import *
from argparse import ArgumentParser
from configparser import ConfigParser

parser = ArgumentParser(description='Centraliza la administracion de los contenedores')

parser.add_argument('-l','--list',help='Lista todos los contenedores',action='store_true')
parser.add_argument('--host',help='Lista los contenedores del servidor indicado',nargs='*')
parser.add_argument('-a','--hidden',help='Muestra contenedores detenidos',action='store_true')
parser.add_argument('-s','--search',help='Busca entre todos los contenedores',nargs=1)
parser.add_argument('--run',help='start/stop contenedor',nargs=2)

args = parser.parse_args()



if debug == "yes":
	print('List: '+str(args.list))
	print('Host: '+str(args.host))
	print('Search: '+str(args.search))
	print('Hidden: '+str(args.hidden))
	print('Run: '+str(args.run))

# show yes/not stop containers
oculto=False
try:
	if args.hidden == True:
		oculto=True
except Exception as e:
	pass
#List dockers
if args.list == True:
	if not args.host == None:
		print(titulo)
		try:
			for y in args.host: 			
				funciones.dockerlist(sudo,y,config.get('HOST',y),oculto)
		except Exception as e:
			print(e)
	else:
		for h in config.items("HOST"):	
			print (titulo)
			funciones.dockerlist(sudo,h[0],h[1],oculto)
#Search Container
if not args.search == None:
	for h in config.items("HOST"):
		funciones.dockersearch(sudo,h[0],h[1],args.search[0],oculto)

if not args.run == None:
	#try:
	for host in args.host:
		funciones.dockerstat(sudo,config.get('HOST',host),args.run[0],args.run[1])
	#except:
		#print("Debe agregar el host con: --host host")
