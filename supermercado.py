#kevin llanca-amaro lezana
#3-D
#17/11/25
#PBD


#Funcion que devuelve el nombre del producto mas caro
def productoMasCaro(productos):
    mayor_precio= -1
    nombre_mayor= ""

    #Recorremos cada linea del archivo
    for linea in productos:
        datos= linea.strip().split(",")  #Separamos por coma
        if len(datos) < 4:
            continue  #Evita errores si una linea viene incompleta

        _, nombre, precio, _ = datos
        precio= int(precio)

        #Comprobamos si este producto es mas caro
        if precio > mayor_precio:
            mayor_precio= precio
            nombre_mayor= nombre

    return nombre_mayor


#Funcion que calcula el valor total de la bodega (precio * cantidad)
def valorTotalBodega(productos):
    total= 0

    for linea in productos:
        datos= linea.strip().split(",")
        if len(datos) < 4:
            continue

        _, _, precio, cantidad=datos
        total += int(precio) * int(cantidad)  #Multiplica precio por unidades en bodega

    return total


#Funcion que encuentra el producto con mas ingresos
#ingresos=precio * cantidad vendida
def productoConMasIngresos(items, productos):
    precios= {}
    nombres= {}

    #Cargar precios y nombres de productos en diccionarios
    for linea in productos:
        datos= linea.strip().split(",")
        if len(datos) < 4:
            continue
        idp, nombre, precio, _ = datos
        precios[idp]=int(precio)
        nombres[idp]=nombre

    ingresos= {}

    #Calcular ingresos por producto
    for linea in items:
        datos= linea.strip().split(";")
        if len(datos) < 3:
            continue

        _, idp, cantidad= datos
        cantidad= int(cantidad)

        if idp not in ingresos:
            ingresos[idp] = 0

        ingresos[idp] += precios[idp] * cantidad

    #Encontrar el ID del producto con más ingresos
    id_mayor= max(ingresos, key=ingresos.get)
    return nombres[id_mayor]


#Funcion que calcula el total de ventas de un mes y año específico
def totalVentasDelMes(año, mes, items, productos, ventas):
    precios= {}

    #Cargar precios de productos
    for linea in productos:
        datos = linea.strip().split(",")
        if len(datos) < 4:
            continue
        idp, _, precio, _ = datos
        precios[idp]= int(precio)

    #Guardar las boletas del mes/año pedido
    boletas= set()
    for linea in ventas:
        num, fecha, _ = linea.strip().split(";")
        dia, m, a = fecha.split("-")

        if int(m) == mes and int(a) == año:
            boletas.add(num)

    #Sumar ventas de esas boletas
    total= 0
    for linea in items:
        num, idp, cantidad= linea.strip().split(";")
        if num in boletas:
            total += precios[idp] * int(cantidad)

    return total

#Llamamos a cada funcion usando los archivos CSV
with open("productos.csv") as p:
    caro= productoMasCaro(p)

with open("productos.csv") as p:
    total_bodega= valorTotalBodega(p)

with open("productos.csv") as p, open("items.csv") as i:
    mas_ingresos= productoConMasIngresos(i, p)

with open("productos.csv") as p, open("items.csv") as i, open("ventas.csv") as v:
    total_mes= totalVentasDelMes(2010, 10, i, p, v)

#Crear archivo informe.txt con los resultados
with open("informe.txt", "w") as f:
    f.write(f"El producto más caro es {caro}\n")
    f.write(f"El valor total de la bodega es de ${total_bodega}\n")
    f.write(f"El producto con más ingresos es {mas_ingresos}\n")
    f.write(f"En el período de 10/2010, el total de ventas es de ${total_mes}\n")

