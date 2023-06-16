import random

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
            

    


a=ruleta_aleatoria()
