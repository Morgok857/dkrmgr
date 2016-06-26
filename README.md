# dkrmgr
Version: 0.03

Este es mi script para administrar varios servidores con contenedores Docker.

Entre otras cosas falta mejorar el control de errores de las funciones implementada



#Requiere:
Python 3.4.2

En caso de administrar uno o varios servidores además del localhost es necesario conexión ssh con rsa.

El usuario que se ejecuta el script debe poder tener permisos para ejecutar los comandos de Docker.

Si el usuario requier sudo para ejecutar los comandos de Docker puede ser activado desde el archivo config.cfg (Activado por defecto)

#Comandos

Listar todos los contenedores:  python3 main.py -l

Para especificar sobre que host se esta trabajando: --host  Ej: python3 main.py --host localhost

Listar contenedores de un host: python3 main.py -l --host localhost

En caso de querer ver los contedores que estan detendidos agregar: -a  Ej:  python3 main.py -l -a

Para buscar un contenedor: -s "nombre del contenedor o Id del contenedor"  Ej:  python3 main.py -s micontenedor
(Por defecto no busca entre los contenedores detenidos. Para agregarlos usar: -a)

En caso de necesitar Detener, Iniciar o ver el estado de un contenedor: --run  (requiere --host) Ej: python3 main.py --host localhost --run d4cdfe4d54a2 status
