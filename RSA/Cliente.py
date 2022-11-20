#LABORATORIO 6
#Nombres: Catalina Ledesma y Denisse Torres

#Cliente

import Funciones
import socket

mensaje_decifrar = []

Host = "LocalHost"
Puerto = 8000

Mi_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Mi_Socket.connect((Host, Puerto))

Mensaje_1 = "Recibida variable e\n"
Mensaje_2 = "Recibida llave n\n"
Mensaje_3 = "fi de n recibido\n"
Mensaje_4 = "Mensaje recibido, ahora procedere a descifrar\n"

for i in range(1):    
    e = Mi_Socket.recv(1024)
    e = int(e.decode(encoding = "ascii", errors = "ignore"))
    
    Mi_Socket.send(Mensaje_1.encode(encoding="ascii", errors="ignore"))
 
    n = Mi_Socket.recv(1024)
    n = int(n.decode(encoding = "ascii", errors = "ignore"))

    Mi_Socket.send(Mensaje_2.encode(encoding="ascii", errors="ignore"))
   
for i in range(1):
    fi_n = Mi_Socket.recv(1024)
    fi_n = int(fi_n.decode(encoding = "ascii", errors = "ignore"))
    
    Mi_Socket.send(Mensaje_3.encode(encoding="ascii", errors="ignore"))

    mensaje_cifrar = Mi_Socket.recv(1024)
    mensaje_cifrar = Mensaje_Cifrado.decode(encoding = "ascii", errors = "ignore")
    
    Mi_Socket.send(Mensaje_4.encode(encoding="ascii", errors="ignore"))
    

mensaje_cifrar = mensaje_cifrar.split(",")
mensaje_cifrar.pop()

for pos in range(0, len(mensaje_cifrar)):
    mensaje_cifrar[pos] = int(mensaje_cifrar[pos])

d = Funciones.modinv(e, fi_n)  #Llave privada

#Descifrado
for m in mensaje_cifrar:
    descifrado = pow(m, d) % n
    mensaje_decifrado.append(decifrado)


print("Decifrado en ASCII:", mensaje_decifrado, "\n")

decifrado = ""

for i in mensaje_decifrado:
    decifrado += chr(i)
    
print("Decifrado:", decifrado)

salida = open('mensajerecibido.txt','w')
salida.write(decifrado)
salida.close()
