#LABORATORIO 6
#Nombre: Catalina Ledesma y Denisse Torres

#RSA

import Funciones

Letras_Ascii = []
Mensaje_Cifrado = []
Mensaje_Descifrado = []

Entrada = open('mensajeentrada.txt','r') #Txt que contiene el texto plano

for i in Entrada.read():
    Letras_Ascii.append(ord(i))
#TextoPlano = Entrada.readlines()[0] #Extrae el texto plano del archivo
Entrada.close()

print(Letras_Ascii,"\n")
    
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
for m in Letras_Ascii:
    Cifrado = pow(m, e) % n
    Mensaje_Cifrado.append(Cifrado)

#Descifrado
for m in Mensaje_Cifrado:
    Descifrado = pow(m, d) % n
    Mensaje_Descifrado.append(Descifrado)


print("Decifrado en ASCII:", Mensaje_Descifrado, "\n")

Descifrado = ""

for i in Mensaje_Descifrado:
    Descifrado += chr(i)
    
print("Decifrado:", Descifrado)
