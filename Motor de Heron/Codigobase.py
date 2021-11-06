import math as mt

while True:
    try:
        op=int(input("¿De cuantos watts es el bombillo que quiere encender?:\n1. 1 watt\n2. 3 watts\n3. 6 watts\n--->"))
        if 1<=op<=3:
            break
        else:
            print("-------------------------\nIngrese una opcion valida\n-------------------------")
    except:
        print("-------------------------\nIngrese una opcion valida\n-------------------------")
        continue

while True:    
    try:
        t=float(input("¿Por cuanto tiempo lo quiere mentener encendido (segundos): "))
        if t>0:
            break
        else:
            print("-------------------------\nIngrese un valor valido\n-------------------------")
    except:
        print("-------------------------\nIngrese un valor valido\n-------------------------")
        continue

m=4 #Masa en kilogramos
r=0.15 #Radio en metros
fr= 150/40 #Frecuencia en radianes/segundos

i= (0.4)*m*(r**2) #Inercia

v_an=2*mt.pi*fr**2 #Velocidad angular

Ecr= (0.5)*(v_an**2)*(i) #Energia cinetica de rotacion
Ecr*=150

p=Ecr/t #Potencia calorica

if op==1:
    if p>=1:
        print("El motor logro encender el bombillo")
    else:
        print("el motor no produce la energia suficiente para encender el bombillo")
elif op==2:
    if p>=3:
        print("El motor logro encender el bombillo")
    else:
        print("el motor no produce la energia suficiente para encender el bombillo")
else:
    if p>=6:
        print("El motor logro encender el bombillo")
    else:
        print("el motor no produce la energia suficiente para encender el bombillo")