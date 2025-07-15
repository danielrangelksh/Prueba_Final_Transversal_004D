productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}

def stock_marca(marca):
    #Función que te muestra el stock de la marca.
            
    encontrados= False
    for modelo, datos in productos.items():
        if datos[0].lower() == marca.lower():
            if stock.get(modelo, [0,0])[1]>0:
                print(f"{modelo}: ${stock[modelo][0]}, Stock: {stock[modelo][1]}")
                encontrados=True  
    if not encontrados:
        print("No hay notebooks con el nombre de esa marca...")

def busqueda_precio(p_min, p_max):
    #Funcion que permite buscar productos mediante su precio.
    try:
        p_min=int(p_min)
        p_max=int(p_max)
    except ValueError:
        print("No hay de ese rango")
        return
    
    modelos_encontrados=[]
    for modelo, datos in stock.items():
        precio, cantidad = datos
        if cantidad > 0 and p_min <= precio <= p_max:
            modelos_encontrados.append(modelo)
            print (modelos_encontrados, stock[modelo])

        if not modelos_encontrados:
            print("No hay modelos en ese rango de precio.")
            return

def actualizar_precio (modelo, precio_nuevo):
    #Función que permite actualizar los precios
    if modelo not in stock:
        print("Modelo no encontrado.")
        return False
    
    stock[modelo][0] = precio_nuevo
    print("Precio actualizado!")
    return True

def menu():
    #Función menú de opciones. 
    while True:
        print("***MENU PRINCIPAL***")
        print("[1] Stock marca.")
        print("[2] Búsqueda por precio.")
        print("[3] Actualizar precio.")
        print("[4] Salir.")

        try:
            opcion=int(input("Ingrese una opción: "))
        except ValueError:
            print("Ingrese un número entero positivo.")
            continue

        if opcion == 1:
            marca=input("Ingrese la marca a buscar: ")
            stock_marca(marca)
        elif opcion == 2:
            try:
                p_min=int(input("Ingrese un precio mínimo: "))
                p_max=int(input("Ingrese un precio máximo: "))
                busqueda_precio(p_min, p_max)
            except ValueError:
                print("Ingrese números enteros positivos.")
                continue
        elif opcion == 3:
            modelo=input("Ingrese el modelo: ")
            if modelo not in productos:
                print("No existe el modelo")
                continue
            
            try:
                precio_nuevo=int(input("Ingrese el nuevo precio: "))
                actualizado=actualizar_precio(modelo, precio_nuevo)
                if actualizado:
                    confirmar=input("Desea actualizar el stock? (s/n): ")
                    if confirmar == "s":
                        nuevo_stock=int(input("Ingrese el stock: "))
                        stock[modelo][1]=nuevo_stock
                        print("El stock se ha actualizado!")
            except ValueError:
                print("Ingrese un número entero positivo.")
                continue
        elif opcion == 4:
            print("Cerrando programa...")
            break
        else:
            print("Ingrese una opción válida (1-4)")
            continue

menu()
        

    
