# dkrmgr
Version: 0.04

Este es mi script para administrar varios servidores con contenedores Docker.

Entre otras cosas falta mejorar el control de errores de las funciones implementada



##Requiere:
Python 3.4.2

En caso de administrar uno o varios servidores además del localhost es necesario conexión ssh con rsa.

El usuario que se ejecuta el script debe tener permisos para ejecutar los comandos de Docker.

Si el usuario requier sudo para ejecutar los comandos de Docker puede ser activado desde el archivo config.cfg (Activado por defecto)

##Comandos

Listar todos los contenedores:  -l
Ej: python3 main.py -l

Para especificar el host que debe usar: --host host
Ej: python3 main.py --host localhost

Listar contenedores de un host: -l --host host
Ej: python3 main.py -l --host localhost

Mostrar contenedores detenidos: -a   
Ej:  python3 main.py -l -a

Para buscar un contenedor: -s "nombre del contenedor o Id del contenedor"
Ej:  python3 main.py -s micontenedor
(Por defecto no busca entre los contenedores detenidos. Para agregarlos usar: -a)

Ineractuar con un contenedor: --run "Id del contenedor" accion    (Se debe especificar el host)

Posibles acciones:
-start	Inicia el contenedor
-stop   Detiene el contenedor 
-status Muestra el estado del contenedor
-ports  Muestra los puertos en uso/expuestos por el contenedor 
-internalip Muesta la ip interna del contenedor

Ej: python3 main.py --host localhost --run d4cdfe4d54a2 status



##Changelog

>Version: 0.04.
Reorganizacion de codigo.
Mejora en el control de errores.
>Se agregaron 2 acciones para --run
