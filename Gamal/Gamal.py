#LABORATORIO 6
#Nombres: Catalina Ledesma y Denisse Torres

#Gamal

letras_ascii = []
mensaje_cifrar = []
mensaje_decifrar = []
mensaje = open('mensajeentrada.txt','r') #Txt que contiene el texto

for i in mensaje.read():
    letras_ascii.append(ord(i))
mensaje.close()

print(letras_ascii,"\n")
    
#Público
P = 199
G = 70 #Alpha
A = 13 #Clave Privada Emisor
k = pow(G,A) % P #Clave pública

print("La clave pública: (G,P,k) =(", G,",", P,",", k,")\n")

cifrado =  ""

#Cifrado
B = 45 #Clave Privada Receptor
y1 = pow(G,B) % P

for i in letras_ascii:
    m = i
    y2 = pow(k,B)*m % P
    mensaje_cifrar.append(y2)
    cifrado += chr(y2)
    
print("Cifrado en ELGAMAL es: ", mensaje_cifrar,"\n")
print("Cifrado: ", cifrado, "\n")
print("Cb(",letras_ascii,",",B,") = (",y1,",",mensaje_cifrar,")\n")

#Decifrado
for i in mensaje_cifrar:
    y2 = i
    m = (pow(y1,(P-1-A))*y2) % P
    mensaje_decifrar.append(m)

print("Decifrado en ASCII: ", mensaje_decifrar, "\n")

decifrado = ""

for i in mensaje_decifrar:
    decifrado += chr(i)
    
print("Decifrado es: ", decifrado)
