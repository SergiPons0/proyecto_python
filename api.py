import requests

# Hacemos una solicitud GET a la API para obtener los datos de usuarios
response = requests.get('https://jsonplaceholder.typicode.com/users')

# Verificamos que la solicitud haya sido exitosa (código de respuesta 200)
if response.status_code == 200:
    # Obtenemos la lista de usuarios en formato JSON
    users = response.json()

    # Imprimimos la información de cada usuario
    for user in users:
        print(f"ID: {user['id']}")
        print(f"Nombre: {user['name']}")
        print(f"Email: {user['email']}")
        print("--------------------")
else:
    print("Ocurrió un error al obtener los usuarios")
