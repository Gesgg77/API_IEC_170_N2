import requests
from prettytable import PrettyTable

def obtener_posts_api(url):
    tabla_posts = PrettyTable()
    tabla_posts.field_names = ['N°', 'Título', 'Contenido', 'Usuario']
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        listado_posts = respuesta.json()
        for post in listado_posts:
            tabla_posts.add_row([
                post['id'],
                post['title'],
                post['body'],
                post['userId']
            ])
    print(tabla_posts)

def crear_post_api(url):
    user_id = input('ID usuario: ')
    titulo = input('Título: ')
    contenido = input('Contenido: ')
    
    post = {
        "userId": int(user_id),
        "title": titulo,
        "body": contenido
    }
    
    respuesta = requests.post(url, json=post)
    print(respuesta.text, respuesta.status_code)

def modificar_post_api(url):
    user_id = input('Nuevo ID usuario: ')
    titulo = input('Nuevo título: ')
    contenido = input('Nuevo contenido: ')
    
    post = {
        "userId": int(user_id),
        "title": titulo,
        "body": contenido
    }
    
    respuesta = requests.put(url, json=post)
    print(respuesta.text, respuesta.status_code)

def eliminar_post_api(url):
    respuesta = requests.delete(url)
    print(respuesta.text, respuesta.status_code)
