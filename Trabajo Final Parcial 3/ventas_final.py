import os
import pyfiglet
from datetime import datetime

folio = 10000

productos = []

ventas = []

def get_folio():
    folio = len(ventas)-1
    return (ventas[folio])[0]

def buscar_id(id):
    for p in productos:
        idp = p[0]
        if idp == id:
            print("Producto encontrado")
            print("\nID:", p[0])
            print("Nombre:", p[1])
            print("Stock:", p[2])
            print("Raza:", p[3])
            print("Marca:", p[4])
            print("Precio:", p[5])
            return productos.index(p)
    return -1

def leer_productos(archivo):
    productos.clear()
    with open(archivo, 'r') as file:
        for linea in file:
            linea = linea.strip()
            datos = linea.split(',')

            if len(datos) < 6:
                print(f"Línea con formato incorrecto: {linea}")
                continue

            id_producto = datos[0]
            nombre = datos[1]
            stock = datos[2]
            raza = datos[3]
            marca = datos[4]
            precio = datos[5]

            productos.append([id_producto, nombre, stock, raza, marca, precio])

    return productos

def leer_ventas(archivo):
    ventas.clear()
    with open(archivo, 'r') as file:
        for linea in file:
            linea = linea.strip()
            datos = linea.split(',')

            if len(datos) < 5:
                print(f"Línea con formato incorrecto: {linea}")
                continue

            folio = datos[0]
            fecha = datos[1]
            id = datos[2]
            cantidad = datos[3]
            total = datos[4]

            ventas.append([folio, fecha, id, cantidad, total])

def listar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                print(linea.strip())
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


def mostrar_productos():
    for producto in productos:
        print("ID: ",producto[0], "Producto: ", producto[1], "Stock: ", producto[2], "Mascota: ", producto[3], "Marca: ", producto[4], "Precio: ", producto[5] )

def ultimo_id():
    max_id = 0
    for producto in productos:
        id = producto[0]
        if id.startswith("P"):

            numero_id = int(id[1:])

            if numero_id > max_id:
                max_id = numero_id
    

    nuevo_id_numero = max_id + 1
    nuevo_id = f"P{nuevo_id_numero:03d}" 

    return nuevo_id

opcion = 0

print(pyfiglet.figlet_format("  Pet shop misifu :3"))
print("""Autores: Amaro Ulloa (✿◦’ᴗ˘◦)♡ 
         Alejandra Toledo =^._.^= """)
os.system("pause")
while opcion != 5:
    os.system("cls")

    print("""
           ≽^-˕-^≼ SISTEMA DE VENTAS ACCESORIOS MASCOTAS ≽^-˕-^≼
                    -----------------------------------
                        1. Vender Productos
                        2. Reportes.
                        3. Mantenedores
                        4. Adminitraciòn
                        5. Salir    
           """)
    
    try:
        opcion = int(input("Ingrese una opcion entre 1-5: "))
        
        if opcion == 1:
            while True:
                os.system("cls")
                print("     Venta de productos   ")
                mostrar_productos()
                id = input("Ingrese ID: ")
                for p in productos:
                    idp = p[0]
                    if idp == id:
                        os.system("cls")
                        print("Producto encontrado")
                        print("\nID:", p[0])
                        print("Tipo:", p[1])
                        print("Stock:", p[2])
                        print("Raza:", p[3])
                        print("Marca:", p[4])
                        print("Precio:", p[5])
                        os.system("pause")
                        try:
                            cantidad = int(input("Ingrese cantidad a comprar: "))
                            stock_producto = int(p[2])
                            if cantidad <= stock_producto and cantidad > 0:
                                print("Stock disponible")
                                total = cantidad * int(p[5])
                                fecha = datetime.now().strftime("%d-%m-%Y")

                                respuesta = input("¿Desea realizar la compra? s/n: ")

                                if respuesta.lower() == "s":
                                    p[2] = str(int(p[2]) - cantidad)  # Stock Actualizado
                                    folio = get_folio()
                                    folio = int(folio)
                                    folio= folio+1
                                    ventas.append([folio, fecha, id, cantidad, total])
                                    print("Compra realizada con éxito.")
                                    os.system("pause")

                            elif cantidad == 0:
                                print("0 el valor ingresado debe ser mayor a 0!")
                            
                            else:
                                print("Error, la cantidad ingresada supera el límite de Stock")
                                os.system("pause")
                        except ValueError:
                            print("Error, la cantidad debe ser un número entero.")
                            os.system("pause")
                        break
                else:
                    print("Producto no encontrado.")
                    os.system("pause")

                respuesta2 = input("¿Desea comprar otro producto? s/n: ")
                if respuesta2.lower() == "n":
                    break

                os.system("pause")
        
        elif opcion == 2:
            os.system("cls")
            op = 0
            while op != 4:
                os.system("cls")
                print("""
                            REPORTES
                    
                    1. Generar reporte de ventas (con total)
                    2. Ventas por fecha especifica 
                    3. Ventas por rango de fecha
                    4. Salir al menu principal
                    """)
                op = int(input("Ingrese una opcion 1-4: "))

                if op == 1:
                    print("Ventas")
                    total = 0
                    for venta in ventas:
                        print(venta[0], "", venta[1], "", venta[2], "", venta[3])
                        total += float(venta[4])
                    print("Total=", total)
                    os.system("pause")

                elif op == 2:
                    fecha = input("Ingrese la fecha de venta (dd-mm-aaaa): ")
                    total = 0
                    for venta in ventas:
                        if venta[1] == fecha:
                            print(venta[0], "", venta[1], "", venta[2], "", venta[3])
                            total += float(venta[4])
                    print("Total=", total)
                    os.system("pause")

                elif op == 3:
                    fechaI_str = input("Ingrese la fecha de inicio (dd-mm-aaaa): ")
                    fechaT_str = input("Ingrese la fecha de termino (dd-mm-aaaa): ")

                    fechaI = datetime.strptime(fechaI_str, "%d-%m-%Y")
                    fechaT = datetime.strptime(fechaT_str, "%d-%m-%Y")

                    total = 0

                    for venta in ventas:
                        fecha_venta = datetime.strptime(venta[1], "%d-%m-%Y")
                        if fechaI <= fecha_venta <= fechaT:
                            print(venta[0], "", venta[1], "", venta[2], "", venta[3])
                            total += float(venta[4])

                    print("Total=", total)
                    os.system("pause")

                elif op == 4:
                    break

        elif opcion == 3:
            os.system("cls")
            op = 0
            while op != 6:
                print("""
                        MANTENEDOR DE PRODUCTOS
                    .........................
                    1. Agregar
                    2. Buscar
                    3. Eliminar
                    4. Modificar
                    5. Listar
                    6. Salir al menù principal             
                    """)
                op = int(input("Ingrese una opcion 1-6: "))

                os.system("cls")

                if op == 1:
                    print("\nAgregar Accesorios\n")
                    
                    id_producto = ultimo_id()
                    producto = input("Ingrese el producto: ")
                    stock_producto = int(input("Ingrese el Stock del producto: "))
                    tipo_animal = input("Ingrese para que animal es el producto: ")
                    marca = input("Ingrese marca del producto: ")
                    precio_producto = float(input("Ingrese el precio del producto: "))

                    productos.append([id_producto, producto, stock_producto, tipo_animal, marca, precio_producto])
                    print("Listo, accesorio agregado!")
                    os.system("Pause")

                elif op == 2:
                    id = input("\n Ingrese ID para buscar producto: \n")
                    i = buscar_id(id)

                    if i != -1:
                        print("ID producto encontrado en el indice ", i)
                        p = productos[i]
                        print("ID:", p[0])
                        print("Nombre:", p[1])
                        print("Stock:", p[2])
                        print("Raza:", p[3])
                        print("Marca:", p[4])
                        print("Precio:", p[5])
                    else:
                        print("Error, ID no existe")
                    os.system("Pause")

                elif op == 3:
                    id_producto = input("Ingrese un ID de producto a eliminar: ")
                    i = buscar_id(id_producto)

                    if i != -1:
                        print("Producto encontrado:")
                        p = productos.pop(i)
                        print("ID:", p[0])
                        print("Nombre:", p[1])
                        print("Stock:", p[2])
                        print("Raza:", p[3])
                        print("Marca:", p[4])
                        print("Precio:", p[5])
                        print("Producto eliminado exitosamente.")
                    else:
                        print("Error, ID de producto no identificado.")
                    os.system("Pause")

                elif op == 4:
                    id_producto = input("Ingrese el codigo del producto a modificar: ")
                    i = buscar_id(id_producto)
                    if i != -1:
                        print("ID encontrado en el indice ", i)
                        p = productos[i]
                        print("ID:", p[0])
                        print("Nombre:", p[1])
                        print("Stock:", p[2])
                        print("Raza:", p[3])
                        print("Marca:", p[4])
                        print("Precio:", p[5])
                        print("\n")
                        nuevo_producto = input("Ingrese el nuevo producto: ")
                        nuevo_stock_producto = int(input("Ingrese el nuevo stock del producto: "))
                        nuevo_tipo_animal = input("Ingrese el nuevo tipo de animal: ")
                        nueva_marca = input("Ingrese la nueva marca: ")
                        nuevo_precio_producto = float(input("Ingrese el nuevo precio: "))

                        productos[i] = [p[0], nuevo_producto, nuevo_stock_producto, nuevo_tipo_animal, nueva_marca, nuevo_precio_producto]

                        print("Listo, datos modificados.")
                    else:
                        print("Error, ID no encontrada.")
                    os.system("Pause")

                elif op == 5:
                    for p in productos:
                        print("ID:", p[0])
                        print("Nombre:", p[1])
                        print("Stock:", p[2])
                        print("Raza:", p[3])
                        print("Marca:", p[4])
                        print("Precio:", p[5])
                        print("\n")
                    os.system("Pause")

                elif op == 6:
                    break

        elif opcion == 4:
            os.system("cls")
            op = 0
            while op != 3:
                print("""     Administraciòn

                    1-Cargar Datos
                    2-Respaldar Datos
                    3-Salir  
                    """)
                op = int(input("Ingrese una opcion 1-3: "))

                if op == 1:
                    print("Cargar Datos")
                    archivo = "productos.txt"
                    archivo_2 = "ventas_productos.txt"
                    leer_productos(archivo)
                    leer_ventas(archivo_2)
                    print("Datos cargados!")
                    os.system("pause")

                elif op == 2:
                    print("Respaldar Datos")
                    archivo_productos = "productos.txt"
                    archivo_ventas = "ventas_productos.txt"

                    # Respaldar productos
                    with open(archivo_productos, "w") as file:
                        for producto in productos:
                            linea = ','.join(map(str, producto))  
                            file.write(linea + '\n')

                    
                    with open(archivo_ventas, "w") as file:
                        for venta in ventas:
                            linea = ','.join(map(str, venta))  
                            file.write(linea + '\n')

                    print("Datos respaldados correctamente.")
                    os.system("pause")



                elif op == 3:
                    break

        elif opcion == 5:
            print("Fin del menú")
            break

    except Exception as e:
        print(f"Error: {e}")
        os.system("pause")

else:
    print("Ingrese una opcion valida! ")
    os.system("pause")
