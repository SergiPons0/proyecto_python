import tkinter as tk
from PIL import ImageTk, Image
import requests
from io import BytesIO

def mostrar_imagen():
    url = url_entry.get()  # Obtiene la URL de la imagen desde el campo de entrada
    response = requests.get(url)  # Realiza una solicitud GET a la URL para obtener los datos de la imagen
    img_data = response.content  # Obtiene los datos de la imagen
    img = Image.open(BytesIO(img_data))  # Crea un objeto de imagen a partir de los datos obtenidos
    img = img.resize((300, 300))  # Ajusta el tamaño de la imagen si es necesario
    img_tk = ImageTk.PhotoImage(img)  # Crea un objeto ImageTk a partir de la imagen para poder mostrarla en la interfaz
    imagen_label.configure(image=img_tk)  # Configura la etiqueta de imagen para mostrar la imagen
    imagen_label.image = img_tk  # Guarda una referencia al objeto ImageTk para evitar que sea eliminado por el recolector de basura

# Crear ventana
ventana = tk.Tk()
ventana.title("Visor de Imágenes")

# Etiqueta y campo de entrada para la URL
url_label = tk.Label(ventana, text="Ingrese la URL de la imagen:")
url_label.pack()
url_entry = tk.Entry(ventana)
url_entry.pack()

# Botón para mostrar la imagen
mostrar_boton = tk.Button(ventana, text="Mostrar Imagen", command=mostrar_imagen)
mostrar_boton.pack()

# Etiqueta para mostrar la imagen
imagen_label = tk.Label(ventana)
imagen_label.pack()

ventana.mainloop()

