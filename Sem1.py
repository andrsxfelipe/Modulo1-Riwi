producto = input("Ingrese el nombre del producto ")
precioProd = float(input("Ingrese el precio del producto "))
if precioProd  >= 0:
    cant = int(input("Ingrese la cantidad de productos "))
    if cant > 0:
        descuento = int(input("Ingrese el valor del descuento (de 0 a 100) "))
        if (descuento>=0) and (descuento<=100):
            if descuento !=0:
                print("El costo del producto ",producto," antes de descuento es de: ",precioProd*cant)
                print("El costo total del producto ",producto," es de: ",precioProd*cant*(1-(descuento/100)))
            else:
                print("El costo total del producto ",producto," es de: ",precioProd*cant)
        else:
            print("Ingrese un descuento entre 0 y 100")
    else:
        print("Ingrese una cantidad válida")
else:
    print("Ingrese un valor válido de producto")


