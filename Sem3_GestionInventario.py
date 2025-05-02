def anadir():
    nom=input("Ingrese el nombre del producto: ")
    prec=float(input("Ingrese el precio: "))
    cant=int(input("¿Qué cantidad hay del producto?: "))
    inventario[nom]=[prec,cant]
    print(inventario)
def consultar():
    prod=input("Ingrese el producto que desea consultar: ")
    try:
        precio = inventario[prod][0]
        cantidad = inventario[prod][1]
        print(f"Precio: {precio}, Cantidad: {cantidad}")
    except KeyError:
        print("El producto no se encuentra en el inventario")
def actPrecios():
    print(inventario.keys())
    prod=input("¿A qué producto desea actualizar el precio?: ")
    if prod in list(inventario.keys()):
        prec=float(input("Ingrese el precio actualizado: "))
        inventario[prod][0]=prec
        print(inventario)
    else:
        print("Producto no se encuentra en el inventario.")
def eliminar():
    prod=input("Ingrese el producto que desea eliminar: ")
    try:
        del inventario[prod]
        print(inventario)
    except:
        print("El producto no se encuentra en el inventario")
def valorTot():
    valorTot=sum(map(lambda x: x[0]*x[1], inventario.values()))
    print(f"El valor total del inventario es de {valorTot} cop")
inventario={}
funcion = int(input("¿Qué desea hacer? (1 para añadir un producto, 2 para consultar un producto, 3 para actualizar el precio de un producto, 4 para eliminar un producto ó 5 para mostrar el valor del inventario, otro para salir): "))
while (funcion>=1) and (funcion<=5):
    if funcion==1:
        anadir()
    elif funcion==2:
        consultar()
    elif funcion==3:
        actPrecios()
    elif funcion==4:
        eliminar()
    else:
        valorTot()
    funcion = int(input("¿Qué desea hacer? (1 para añadir un producto, 2 para consultar un producto, 3 para actualizar el precio de un producto, 4 para eliminar un producto ó 5 para mostrar el valor del inventario, otro para salir): "))