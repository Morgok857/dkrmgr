#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys,os
from configparser import ConfigParser

diripath = os.path.dirname(os.path.realpath(__file__))
hostlis = {}

# Config read
pathcfg = diripath+"/config.cfg"
config = ConfigParser()
config.read(pathcfg)

# Show version and test access to config file
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

#Config degug stats
if config.get('GENERAL','debug') == "yes":
	debug="yes"
else:
	debug="false"

