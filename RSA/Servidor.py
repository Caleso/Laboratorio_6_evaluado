#LABORATORIO 6
#Nombre: Catalina Ledesma y Denisse Torres

#Servidor

import Funciones
import socket

letras_ascii = []
mensaje_cifrar = ""
mensaje = open('mensajeentrada.txt','r') #Txt que contiene el texto

for i in mensaje.read():
    letras_ascii.append(ord(i))
mensaje.close()

#Primos privados
P = 569
Q = 839 
n = P*Q #Llave publica
fi_n = (P-1)*(Q-1)

seguir = True
while seguir:
    e = int(input("Ingrese valor de e: "))
    if Funciones.mcd(e, fi_n) == 1:
        seguir = False
    else:
        print("El maximo comun divisor debe ser 1")
        

#Cifrado
for m in letras_ascii:
    cifrado = pow(m, e) % n
    mensaje_cifrar += str(cifrado)+","
    
#VARIABLES PUBLICAS: e, n
    
#VARIABLES PRIVADAS: P, Q, fi_n

Host = "LocalHost"
Puerto = 8000

Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Server.bind((Host, Puerto))
Server.listen(1)
print("Servidor en espera\n")

Conexion, Addr = Server.accept()

e = str(e)
n = str(n)
fi_n = str(fi_n)

for i in range(1):
    Conexion.send(e.encode(encoding="ascii", errors="ignore"))
    Mensaje_1 = Conexion.recv(1024)
    print((Mensaje_1.decode(encoding = "ascii", errors = "ignore")))
    
    Conexion.send(n.encode(encoding="ascii", errors="ignore"))
    Mensaje_2 = Conexion.recv(1024)
    print((Mensaje_2.decode(encoding = "ascii", errors = "ignore")))
    
for i in range(1):
    Conexion.send(fi_n.encode(encoding="ascii", errors="ignore"))
    Mensaje_3 = Conexion.recv(1024)
    print((Mensaje_3.decode(encoding = "ascii", errors = "ignore")))
    
    Conexion.send(Mensaje_Cifrado.encode(encoding="ascii", errors="ignore"))
    Mensaje_4 = Conexion.recv(1024)
    print((Mensaje_4.decode(encoding = "ascii", errors = "ignore")))
