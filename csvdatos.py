import csv
import os
import datetime

ruta_base = '/home/pedro/Desktop/archivos/'
datos = ruta_base + 'cust_orders_prods.csv'

def menu():
    limpiar()
    pintar_menu()
    pregunta_usuario(dicc)

def pintar_menu():
    limpiar()
    print("""---------------------Consultas CSV---------------------

    1.- Mostrar porcentaje de ventas de cada vendedor
    2.- Mostrar porcentaje de ventas de cada cliente
    3.- Mostrar los 5 productos más vendidos
    4.- Ingresos mensuales
    5.- Salir
    """)

def pregunta_usuario(dicc):
    opc1 = input("Escriba con un numero lo que quiera realizar: ")
    if opc1 == "1":
        printear_porcentaje_vendedores(dicc)
    
    elif opc1 == "2":
        printear_porcentaje_cliente(dicc)
    
    elif opc1 == "3":
        pintar_top5(dicc)
    
    elif opc1 == "4":
        printear_meses(dicc)
    
    elif opc1 == "5":
        salir()
    else: 
        menu()

def ventas_vendedor(diccionario):
    limpiar()
    dicc_vendedores = {}

    for fila in diccionario:
        vendedor = fila["employee_name"]
        cantidad = int(fila["quantity"])
        precio_ud = int(fila["unit_price"])
        precio_total = cantidad * precio_ud
        if vendedor not in dicc_vendedores:
            dicc_vendedores[vendedor] = precio_total
        else:
            dicc_vendedores[vendedor] = dicc_vendedores[vendedor] + precio_total
    return dicc_vendedores

def porcentaje_vendedores(diccionario):
    dicc_vendedores = ventas_vendedor(diccionario)
    total_ventas = total_vendido(diccionario)
    for j in dicc_vendedores:
        dicc_vendedores[j] = f"{round(((dicc_vendedores[j] / total_ventas) * 100),2)}%"
    return dicc_vendedores

def printear_porcentaje_vendedores(diccionario):
    dicc_vendedores = porcentaje_vendedores(diccionario)
    print("PORCENTAJE VENTAS DE VENDEDORES\n")
    for k, v in dicc_vendedores.items():
        print(f"{k}: {v}")
    volver()

def ventas_cliente(diccionario):
    limpiar()
    dicc_cliente = {}

    for fila in diccionario:
        cliente = fila["customer_name"]
        cantidad = int(fila["quantity"])
        precio_ud = int(fila["unit_price"])
        precio_total = cantidad * precio_ud
        if cliente not in dicc_cliente:
            dicc_cliente[cliente] = precio_total
        else:
            dicc_cliente[cliente] = dicc_cliente[cliente] + precio_total
    return dicc_cliente
        
def porcentaje_cliente(diccionario):
    dicc_cliente = ventas_cliente(diccionario)
    total_ventas = total_vendido(diccionario)
    for j in dicc_cliente:
        dicc_cliente[j] = f"{round(((dicc_cliente[j] / total_ventas)*100),2)}%"

        
    return dicc_cliente

def printear_porcentaje_cliente(diccionario):
    limpiar()
    dicc_cliente = porcentaje_cliente(diccionario)
    print("PORCENTAJE VENTAS DE CLIENTES\n")
    for k, v in dicc_cliente.items():
        print(f"{k}: {v}")
    volver()

def calcular_productos_total(diccionario):
    
    limpiar()
    dicc_productos = {}

    for fila in diccionario:
        producto = fila["product_name"]
        cantidad = int(fila["quantity"])

        if producto not in dicc_productos:
            dicc_productos[producto] = cantidad
        else:
            dicc_productos[producto] += cantidad
    
    return dicc_productos

def calcular_top5(diccionario):
    dicc_productos = calcular_productos_total(diccionario)
    top5 = {}
    for i in range (5):
        max_value = max(dicc_productos, key=dicc_productos.get)
        top5[max_value] = dicc_productos[max_value] 
        del dicc_productos[max_value]

    return top5

def pintar_top5(diccionario):
    limpiar()
    top5 = calcular_top5(diccionario)
    print(f"LOS 5 PRODUCTOS MÁS VENDIDOS\n")
    for i in top5:
        print(f"{i} - {top5[i]}")
    volver()

def ordena_diccionario(diccionario):
    dicc_ordenado = dict(sorted(diccionario.items()))
    return dicc_ordenado

def numero_nombre(diccionario):
    dicc = {}
    for i in range(12):
        if i == 1 and i in diccionario:
            dicc["Enero"] = diccionario[1]
        elif i == 2 and i in diccionario:
            dicc["Febrero"] = diccionario[2]
        elif i == 3 and i in diccionario:
            dicc["Marzo"] = diccionario[3]
        elif i == 4 and i in diccionario:
            dicc["Abril"] = diccionario[4]
        elif i == 5 and i in diccionario:
            dicc["Mayo"] = diccionario[5]
        elif i == 6 and i in diccionario:
            dicc["Junio"] = diccionario[6]
        elif i == 7 and i in diccionario:
            dicc["Julio"] = diccionario[7]
        elif i == 8 and i in diccionario:
            dicc["Agosto"] = diccionario[8]
        elif i == 9 and i in diccionario:
            dicc["Septiembre"] = diccionario[9]
        elif i == 10 and i in diccionario:
            dicc["Octubre"] = diccionario[10]
        elif i == 11 and i in diccionario:
            dicc["Noviembre"] = diccionario[11]
        elif i == 12 and i in diccionario:
            dicc["Diciembre"] = diccionario[12]

    return dicc

def fecha_hora(diccionario):

    dicc_fechas = {}

    for fila in diccionario:
        fecha_hora = fila["order_date"]
        fecha_hora_partida = datetime.datetime.strptime(fecha_hora,"%Y-%m-%d %H:%M:%S")
        mes = fecha_hora_partida.month

        cantidad = int(fila["quantity"])
        precio_ud = int(fila["unit_price"])
        precio_total = cantidad * precio_ud
        if mes not in dicc_fechas:
            dicc_fechas[mes] = precio_total
        else:
            dicc_fechas[mes] = dicc_fechas[mes] + precio_total

    dicc_ordenado = ordena_diccionario(dicc_fechas)
    dicc_salida = numero_nombre(dicc_ordenado)

    return dicc_salida

def printear_meses(diccionario):
    limpiar()
    dicc_meses = fecha_hora(diccionario)
    print("INGRESOS POR MES\n")
    for k, v in dicc_meses.items():
        print(f"{k}: {v}€")
    volver()

def total_vendido(diccionario):
    total_ventas = 0
    for i in range(len(diccionario)):
        total_ventas += int(diccionario[i]['quantity'])*int(diccionario[i]['unit_price'])
    return  total_ventas

def volver():
    print("\n")
    volver=input("Pulse enter para volver: ")
    if volver == "":
        menu()
    else:
        menu()

def salir():
    exit()

def limpiar():
    os.system("clear")
    
def abrir_csv(ruta_archivo):
    f = open(ruta_archivo,"r")
    lector_dict = csv.DictReader(f)
    lista_dict = list(lector_dict)
    f.close()
    return lista_dict

dicc = abrir_csv(datos)

print(menu())