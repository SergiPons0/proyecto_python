import random
import os
import tkinter as tk
import requests

def menu():
    print("""
    1. Ruleta Aleatoria
    2. Lista de Tareas
    3. Juego de Adivinanzas
    4. Cargar Imagen
    5. Apy
    0. Salir 
    """)
    x= input("Introduce una opcion del menu: ")
    return x

def ruleta_aleatoria():
    while True:
        opciones=[]
        while True:
            opcion= input("Escribe las opciones para la ruleta aleatoria: ")
            if opcion=='.':
                break
            opciones.append(opcion)
        
        if len(opciones)< 2:
            print("Escribe almenos dos opciones")
            continue
        
        print("Ruleta Preparada para funcionar")

        while True:
            palabra_seleccionada=random.choice(opciones)
            print("La ruleta se ha detenido en la opcion: {}".format(palabra_seleccionada))
            otravez=input("Deseas girar la ruleta de nuevo? s/n: ")
            if otravez.lower() !="s":
                break

        reiniciar=input("Deseas crear una ruleta nueva? s/n: ")
        if reiniciar.lower() !="s":
            break

def guardar_tareas():
    ruta_directorio = os.getcwd() # Obtiene el directorio actual donde se ejecuta el programa
    nombre_archivo = 'lista_tareas.txt'
    ruta_archivo = os.path.join(ruta_directorio, nombre_archivo)
    tareas = []
    while True:
        tarea = input("Ingrese una tarea: ")
        if tarea == '.':
            break
        tareas.append(tarea)
    with open(ruta_archivo, 'w') as archivo:
        for tarea in tareas:
            archivo.write(tarea + '\n')
        print("Tareas guardadas exitosamente.")

def actualizar_tarea():
    ruta_directorio = os.getcwd()
    nombre_archivo = 'lista_tareas.txt'
    ruta_archivo = os.path.join(ruta_directorio, nombre_archivo)
    tarea_vieja = input("Ingrese la tarea que desea actualizar: ")
    tarea_nueva = input("Ingrese la nueva tarea: ")
    with open(ruta_archivo, 'r') as archivo:
        lineas = archivo.readlines()
    with open(ruta_archivo, 'w') as archivo:
        for linea in lineas:
            if linea.strip() == tarea_vieja:
                archivo.write(tarea_nueva + '\n')
            else:
                archivo.write(linea)
    print("Tarea actualizada exitosamente.")

def borrar_tarea():
    ruta_directorio = os.getcwd()
    nombre_archivo = 'lista_tareas.txt'
    ruta_archivo = os.path.join(ruta_directorio, nombre_archivo)
    tarea = input("Ingrese la tarea que desea borrar: ")
    with open(ruta_archivo, 'r') as archivo:
        lineas = archivo.readlines()
    with open(ruta_archivo, 'w') as archivo:
        for linea in lineas:
            if linea.strip() != tarea:
                archivo.write(linea)
    print("Tarea borrada exitosamente.")

def mostrar_tareas():
    ruta_directorio = os.getcwd()
    nombre_archivo = 'lista_tareas.txt'
    ruta_archivo = os.path.join(ruta_directorio, nombre_archivo)
    try:
        with open(ruta_archivo, 'r') as archivo:
            lineas = archivo.readlines()
        for i, linea in enumerate(lineas, start=1):
            print(f"{i}. {linea.strip()}")
    except FileNotFoundError:
        print("El archivo no existe.")


def menu_tareas():
    print("""
    Menu
        1. Guardar tareas
        2. Actualizar tareas
        3. Borrar tareas
        4. Mostrar tareas
        5. Salir
        """)
    x= input("Elije la opcion que quieras: ")
    return x

def adivinanzas():
    print("""
    * Las respuestas tienen que estar contestadas con la primera letra mayúscula *

    - Soy un ave muy colorida,
    Con plumas brillantes y largas,
    En las noches, mi canto es oído,
    ¿Quién soy? 
    
    """)

    respuesta1 = input("Respuesta 1: ")

    while respuesta1 != "Pavo real":
        print("La respuesta 1 es incorrecta. Inténtalo de nuevo.")
        respuesta1 = input("Respuesta 1: ")

    print("""
    - Tengo ramas, pero no hojas,
    Un tronco, pero no es de árbol,
    ¿Qué soy?
     
    """)
    

    respuesta2 = input("Respuesta 2: ")

    while respuesta2 != "Silla":
        print("La respuesta 2 es incorrecta. Inténtalo de nuevo.")
        respuesta2 = input("Respuesta 2: ")

    print("""
    - De noche soy blanco,
    De día me vuelvo negro,
    ¿Quién soy? 
    
    """)

    respuesta3 = input("Respuesta 3: ")

    while respuesta3 != "Búho":
        print("La respuesta 3 es incorrecta. Inténtalo de nuevo.")
        respuesta3 = input("Respuesta 3: ")

    print("""
    - Todos me quieren tocar,
    Pero si me tocan, me destruyen,
    ¿Quién soy? 
    
    """)

    respuesta4 = input("Respuesta 4: ")

    while respuesta4 != "Hielo":
        print("La respuesta 4 es incorrecta. Inténtalo de nuevo.")
        respuesta4 = input("Respuesta 4: ")

    print("¡Todas las respuestas son correctas!")
    return respuesta1, respuesta2, respuesta3, respuesta4

def ventana():
    try: 
        import imagen.py
    except:
        ModuleNotFoundError
        print("Error")


        

#PP
x="1"
while x!=".":
        x = menu()
        match x:
            case "1":
                print("Has elegido la opcion de la ruleta aleatoria" )
                Ruleta=ruleta_aleatoria()

            case "2":
                print("Has elegido la opcion de la lista de tareas")
                while True:
                    p=menu_tareas()
                    match p:
                        case "1": 
                            guardar_tareas()
                        case "2":
                            actualizar_tarea()
                        case "3":
                            borrar_tarea()
                        case "4":
                            mostrar_tareas()
                        case "5":
                            print("Adiós")
                            break
                        case other:
                            print("Opción no válida.")   
            case "3":
                print("Has elegido la opcion de el juego de las adivinanzas")
                Juego=adivinanzas()

            case "4":
                print("Has elegido la opcion de Cargar una imagen ")
                ventanaflotante=ventana()

            case "5":
                print("Has elegido la opcion del api")
                peliculas=apy()

            case "6":
                print("Has elegido la opcion del Servidor Web")
                adsd=apfd()

            case "0": 
                print("Adios")
                x="."

            case other:
                print("Opcion no valida")




