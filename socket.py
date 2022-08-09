# ENVIAR.py" 
# -*- coding: latin-1 -*
import socket              
# Creamos un objeto de clase socket 
s = socket.socket()
# Indicamos el host y el puerto que estar a la escucha con una tupla 
s.bind(("localhost", 9999))
# Metodo listen para aceptar conexiones entrantes # con el numero maximo de conexiones aceptadas 
s.listen(1) 
# Metodo accept para escuchar # Bloquea la ejecucion hasta que llega un mensaje # Cuando este llega, devuelve un objeto socket # y una tupla con el host y el puerto de la conexion 
c, addr_socketc = s.accept() 

print("Conexion desde", addr_socketc)

# Esperamos un mensaje del cliente 
recibido = c.recv(1024) 
print(recibido.decode("utf-8"))
# Cerramos los sockets
c.close()
s.close()
