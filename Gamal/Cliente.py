#LABORATORIO 6
#Nombres: Catalina Ledesma y Denisse Torres

#Cliente

import socket

mensaje_cifrar = ""
letras_ascii = [] #Guarda el mensaje letra a letra en ascii
mensaje = open('mensajeentrada.txt','r') #Txt que contiene el texto plano

for i in mensaje.read():
    letras_ascii.append(ord(i))
mensaje.close()

cifrado =  ""#Almacena el mensaje cifrado
B = int(input("Ingrese el valor de B: "))

Host = "LocalHost"
Puerto = 8000
Mi_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Mi_Socket.connect((Host, Puerto))

for i in range(1):
    P = Mi_Socket.recv(1024)
    P = int(P.decode(encoding = "ascii", errors = "ignore"))
    Mi_Socket.send(b'P recibido por el cliente')
    G = Mi_Socket.recv(1024)
    G = int(G.decode(encoding = "ascii", errors = "ignore"))
    Mi_Socket.send(b'G recibido por el cliente')
    k = Mi_Socket.recv(1024)
    k = int(k.decode(encoding = "ascii", errors = "ignore"))
    Mi_Socket.send(b'k recibido por el cliente')
    print((Mi_Socket.recv(1024)).decode(encoding="ascii", errors="ignore"))
    
    #Mensaje Cifrado
    for m in letras_ascii:
        y2 = pow(k,B)*m % P
        cifrado += chr(y2)

    print("El cifrado es: ", cifrado, "\n")
    
    y1 = pow(G,B) % P #Se envía hacia el servidor
    Mi_Socket.send(str(y1).encode(encoding="ascii", errors="ignore"))
    print("y1 enviado")
    print((Mi_Socket.recv(1024)).decode(encoding="ascii", errors="ignore"))
    
    for i in cifrado:
        mensaje_cifrar += "," + str(ord(i))
        
    Mi_Socket.send(mensaje_cifrar.encode(encoding="ascii", errors="ignore"))#Envia al server el mensaje cifrado en ascii
    
