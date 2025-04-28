## Problema 1 de la pagina 42
import math

##DEFINIMOS FUNCIONES
def cubo_radio(r1,y):
    C3 = r1 ** y
    return C3

def cuadrado_radio(r2,x):
    C2 = r2 ** x
    return C2

def volumen_solido(r1,r2,h):
    vlme_esfe = (4/3) * cubo_radio(r1,3) * math.pi
    vlmn_cono = (1/3) * cuadrado_radio(r2,2) * math.pi * h
    vlmn_solido = vlme_esfe + vlmn_cono 
    print(f"El volumen del solido es igual a {vlmn_solido}m**3")
    return vlmn_solido

def area_figura1(a,b,r2):
    area_reg = a * b
    area_rue = math.pi * cuadrado_radio(r2,2)
    area = area_reg + (2 * area_rue)
    print(f"El area de la figura es igual a {area}m**2")
    return area

def area_figura0(a,b,r2):
    area_reg = a * b
    area_rue = math.pi * cuadrado_radio(r2,2)
    area = area_reg + area_rue
    return area

def area_figura2(b1,h1,b2,h2,r1,r2):
    area_total = area_figura0(b1,h1,r1) + area_figura0(b2,h2,r2)
    print(f"El area de la figura es igual a {area_total}m**2")
    return area_total

def aves(G,M,P):
    kilos = (6*G) + (7*M) + P
    print(f"Los kilos los totales de aves son {kilos}kilos")
    return kilos

def compra(p,B,H):
    valor = (300*p) + (3300*B) + (350*H)
    print(f"Debe pagar {valor}pesos")
    dinero = (float(input("Con que billete va a pagar\n")))
    if(dinero < valor):
        dif = valor - dinero
        print(f"Le faltan {dif}pesos para pagar toda la cuenta")
    elif(dinero > valor):
        dif1 = dinero - valor
        print(f"Estos son sus vueltos {dif1} pesos")
    else:
        print("Pago exactamente el valor de la cuenta")
    return valor 

def prestamo(plata,meses):
    porciento = (plata * 3) / 100
    pagar= plata + (porciento * meses)
    print(f"Debe pagar de intereses {pagar} pesos")
    return pagar 

def covid(C,d):
    conteo=1
    while(conteo <= d):
        C**=2
        conteo+=1
    print(f"Despues de {d} dias se reportan {C} personas contagiadas")
    return C

##LLAMAMOS A LAS FUNCIONES
pregun = (int(input("Dime que ejercicio quieres realizar, para esto dame un número del 1-7\n")))

if(pregun==1):
    volumen_solido(float(input("Dime el r de la esfera en m\n")), float(input("El r del cono en m\n")),float(input("Y la h del cono en m\n ")))

elif(pregun==2):
    area_figura1(float(input("Dime la b del rectangulo en m\n")), float(input("La h del mismo en m\n")),float(input("Y el r de la rueda en m\n ")))

elif(pregun == 3):
    area_figura2(float(input("Dime la b del rectangulo uno en m\n")), float(input("La h de mismo en m\n")),float(input("Ahora la b del rectangulo dos en m\n ")),float(input("La h del mismo en m\n")), float(input("Ademas el r de la rueda uno en m\n")),float(input("Y el r de la rueda dos en m\n ")))

elif(pregun == 4):
    aves(float(input("Dime cuantas galinas hay\n")), float(input("Cuantos gallos\n")),float(input("Y cuantos pollos\n ")))

elif(pregun == 5):
    compra(int(input("Dime cuantos panes va a llevar\n")), int(input("Cuantas bolsas\n")),int(input("Y cuantos huevos\n ")))

elif(pregun == 6):
    prestamo(int(input("Cuanto dinero pidio prestado\n")), int(input("Por cantos meses\n")))

elif(pregun == 7):
    covid(int(input("Cuantos casos reportados de covid hay hoy\n")), int(input("Por cuantos dias quieres hacer la predicción\n")))

else:
    print("Selecciono una opción invalida")