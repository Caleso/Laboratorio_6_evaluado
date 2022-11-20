#LABORATORIO 6
#Nombre: Catalina Ledesma y Denisse Torres

#Servidor

import socket

mensaje_cifrar = []
mensaje_decifrar = []

#Público
P = 199
G = 70 #Alpha, raíz primitiva de P 
A = int(input("Ingrese el valor de A: ")) #Clave Privada Emisor
k = pow(G,A) % P #Clave pública

print("La clave pública: (G,P,k) =(", G,",", P,",", k,")\n")

#Servidor
Host = "LocalHost"
Puerto = 8000

Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Server.bind((Host, Puerto))
Server.listen(1)
print("Servidor en espera\n")

Conexion, Addr = Server.accept()

for i in range(1):
    Conexion.send(str(P).encode(encoding="ascii", errors="ignore"))
    print((Conexion.recv(1024)).decode(encoding="ascii", errors="ignore"))
    Conexion.send(str(G).encode(encoding="ascii", errors="ignore"))
    print((Conexion.recv(1024)).decode(encoding="ascii", errors="ignore"))
    Conexion.send(str(k).encode(encoding="ascii", errors="ignore"))
    print((Conexion.recv(1024)).decode(encoding="ascii", errors="ignore"))
    Conexion.send(b'Solicitar y1')
    
    y1 = Conexion.recv(1024)
    y1 = int(y1.decode(encoding = "ascii", errors = "ignore"))
    Conexion.send(b'Solicitar mensaje encriptado')
    
    cifrado = Conexion.recv(1024)
    cifrado = cifrado.decode(encoding="ascii", errors="ignore")
    print("\n")
    
cifrado = cifrado.split(",")

for i in cifrado:
    if i != "":
        mensaje_cifrar.append(int(i))
   
#Descifrado
for y2 in mensaje_cifrar:
    m = (pow(y1,(P-1-A))*y2) % P
    mensaje_decifrar.append(m)

decifrado = ""

for i in mensaje_decifrar:
    decifrado += chr(i)

mensajito_cifrar = ""

for i in mensaje_cifrar:
    mensajito_cifrar += chr(i)

print("Mensaje Cifrado:", mensajito_cifrar)
print("Mensaje Descifrado:", decifrado)


salida = open('mensajerecibido.txt','w')
salida.write(decifrado)
salida.close()
