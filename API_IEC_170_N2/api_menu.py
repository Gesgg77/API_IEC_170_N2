from negocio.negocio_user import *
from negocio.negocio_post import *

while True:
    print("""
1. Listar usuarios
2. Crear usuario
3. Modificar usuario
4. Eliminar usuario
5. Listar posts
6. Crear post
7. Modificar post
8. Eliminar post
0. Salir
""")

    op = input("Opción: ")

    if op == "1":
        obtener_users_db()
    elif op == "2":
        crear_user_db()
    elif op == "3":
        modificar_user_db()
    elif op == "4":
        eliminar_user_db()
    elif op == "5":
        obtener_posts_db()
    elif op == "6":
        crear_post_db()
    elif op == "7":
        modificar_post_db()
    elif op == "8":
        eliminar_post_db()
    elif op == "0":
        break
    else:
        print("Opción inválida")
