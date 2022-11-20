#LABORATORIO 6
#Nombre: Catalina Ledesma y Denisse Torres

#RSA

import Funciones

letras_ascii = []
mensaje_cifrar = []
mensaje_decifrar = []

mensaje = open('mensajeentrada.txt','r') #Txt que contiene el texto

for i in mensaje.read():
    letras_ascii.append(ord(i))

mensaje.close()

print(letras_ascii,"\n")
    
#Público
P = 569
Q = 839 
n = P*Q
fi_n = (P-1)*(Q-1)

seguir = True
while seguir:
    e = int(input("Ingrese valor de e: "))
    if Funciones.mcd(e, fi_n) == 1:
        seguir = False
    else:
        print("El maximo comun divisor debe ser 1")
        
d = Funciones.modinv(e, fi_n)

#Cifrado
for m in letras_ascii:
    cifrado = pow(m, e) % n
    mensaje_cifrar.append(Cifrado)

#Descifrado
for m in mensaje_cifrar:
    descifrado = pow(m, d) % n
    mensaje_decifrar.append(Descifrado)


print("Decifrado en ASCII:", mensaje_decifrar, "\n")

descifrado = ""

for i in mensaje_decifrar:
    Descifrado += chr(i)
    
print("Decifrado:", descifrado)
