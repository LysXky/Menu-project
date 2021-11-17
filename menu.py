import time

combo1 = 1990
combo2 = 2590
combo3 = 2390
combo4 = 2890
combo5 = 5990

def menu ():
    print ("Este es nuestro menú el día de hoy, " + nombre)
    print ("###############################################")
    print ("|1|>> Completo Italiano --- $1990")
    print ("|2|>> Combo Hamburguesa Americana --- $2.590")
    print ("|3|>> Combo Hamburguesa Pollo --- $2.390")
    print ("|4|>> Combo Mixto Carne y Pollo --- $2.890")
    print ("|5|>> Combo Gigante Mixto --- $5.990")
    print ("###############################################")
    return;

def detallesMenu ():
    print ("opcion 1: Combo  completo  con  bebida  y papas pequeñas")
    print ("opcion 2: Combo con 2 hamburguesas pequeñas tipo americana, papas y bebida mediana")
    print ("opcion 3: Combo  con  2  hamburguesas  de pollo  teriyaki,  ,  papas  y  bebida mediana ")
    print ("opcion 4: Combo con 2 hamburguesas, una  de  carne  y  otra  de  pollo teriyaki, papas y bebida")
    print ("opcion 5: Combo de 2 hamburguesas como  las  desee  el  cliente,  con papas gigantes y bebida XL")

def pedidohecho ():
    cantc1 = 0
    cantc2 = 0
    cantc3 = 0
    cantc4 = 0
    cantc5 = 0
    x = input("Desea ver qué lleva cada menú: Sí o No [S/N] ")
    if x == 's':
        detallesMenu()
        time.sleep(3)
        pedido = input("seleccione el pedido que desea llevar: Presine 0 para continuar>>> ")
    while pedido != "0":
        if pedido == '1':
            cantc1 = (cantc1:=input('cuantos desea llevar: '))
        elif pedido == '2':
            cantc2 = (cantc2:=input('cuantos desea llevar: '))
        elif pedido == '3':
            cantc3 = (cantc3:=input('cuantos desea llevar: '))
        elif pedido == '4':
            cantc4 = (cantc4:=input('cuantos desea llevar: '))
        elif pedido == '5':
            cantc5 = (cantc5:=input('cuantos desea llevar: '))
        pedido = input("seleccione el pedido que desea llevar: Presine 0 para continuar>>> ")    
    else :
        print ("gracias estamos procesando su compra")
        time.sleep(3)
    total = (int(cantc1) * int(combo1) + int(cantc2) * int(combo2) + int(cantc3) * int(combo3) + int(cantc4) * int(combo4) + int(cantc5) * int(combo5))
    print ('el total a pagar son, ' + str(total))

if __name__=="__main__":
    print ("Fast Food")
    nombre = input("Ingrese su nombre: ")
    print ("Bienvenido a nuestra surcursal, " + nombre )
    time.sleep(3)
    menu()
    time.sleep(3)
    pedidohecho()