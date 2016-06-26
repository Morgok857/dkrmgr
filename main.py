#!/usr/bin/python3
import sys,os
import funciones
from argparse import ArgumentParser
from configparser import ConfigParser

diripath = os.path.dirname(os.path.realpath(__file__))
hostlis = {}

pathcfg = diripath+"/config.cfg"
config = ConfigParser()
config.read(pathcfg)
	
try:
	versionn = config.get('GENERAL','version')
	titulo = config.get('GENERAL','columnas')
	print()
	print("Version: "+versionn)
	print()
except:
	print("No se puede leer el archivo de configuracion.")
	sys.exit(1)

if config.get('GENERAL','sudo') == "yes":
	sudo="sudo"
else:
	sudo=""
parser = ArgumentParser(description='Centraliza la administracion de los contenedores')

parser.add_argument('-l','--list',help='Lista todos los contenedores',action='store_true')
parser.add_argument('--host',help='Lista los contenedores del servidor indicado',nargs='*')
parser.add_argument('-a','--hidden',help='Muestra contenedores detenidos',action='store_true')
parser.add_argument('-s','--search',help='Busca entre todos los contenedores',nargs=1)
parser.add_argument('--run',help='start/stop contenedor',nargs=2)

args = parser.parse_args()

try:

	if config.get('GENERAL','debug') == "yes":
		print('List: '+str(args.list))
		print('Host: '+str(args.host))
		print('Search: '+str(args.search))
		print('Hidden: '+str(args.hidden))
		print('Run: '+str(args.run))
except:
	pass

oculto=False
try:
	if args.hidden == True:
		oculto=True
except Exception as e:
	pass

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

if not args.search == None:
	for h in config.items("HOST"):
		funciones.dockersearch(sudo,h[0],h[1],args.search[0],oculto)

if not args.run == None:
	for host in args.host:
		funciones.dockerstat(sudo,config.get('HOST',host),args.run[0],args.run[1])
	
