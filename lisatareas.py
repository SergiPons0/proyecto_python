import os
def crear_archivo():
    nombre_archivo = input("Ingresa el nombre del archivo: ")
    contenido = input("Ingresa el contenido del archivo: ")
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido)
    print("Archivo creado y guardado exitosamente.")

def actualizar_archivo():
    nombre_archivo = input("Ingresa el nombre del archivo a actualizar: ")
    contenido_nuevo = input("Ingresa el nuevo contenido del archivo: ")
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido_nuevo)
    print("Archivo actualizado y guardado exitosamente.")

def borrar_archivo():
    nombre_archivo = input("Ingresa el nombre del archivo a borrar: ")
    try:
        os.remove(nombre_archivo)
        print("Archivo borrado exitosamente.")
    except FileNotFoundError:
        print("El archivo no existe.")

def mostrar_archivo():
    nombre_archivo = input("Ingresa el nombre del archivo a mostrar: ")
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)
    except FileNotFoundError:
        print("El archivo no existe.")

# Ejemplo de uso
crear_archivo()
actualizar_archivo()
borrar_archivo()
mostrar_archivo()
