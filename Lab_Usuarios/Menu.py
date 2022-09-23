#Programa: Lab_Usuarios.py
#Proposito: Modificación de una DB por medio de un Menú interactivo.
#Autor: Ezequiel Lopez
#Fecha: 23/09/2022

from conexion import *
from cursor_pool import *
from logger import *
from usuarios import *
from usuario_dao import *

valor = None
while(valor != 5):
    try:
        print("")
        print("Bienvenido a este Menu".center(50,"_"))
        print("Considere escoger una de las siguientes opciones:")
        print("""        1) Listar Usuarios
        2) Agregar Usuario
        3) Actualizar Usuario
        4) Eliminar Usuario
        5) Salir del Menú""")        
        valor = int(input("Ingrese el numero de la accion a efectuar: "))

        if(valor == 1):
            personas = UsuarioDao().seleccionar()
            for persona in personas:
                log.debug(persona)

        if(valor == 2):
            usuario = Usuario(username=input("Ingrese el nombre del nuevo usuario: "), password=input("Ingrese la password del nuevo usuario: "))
            UsuarioDao().insert(usuario)

        if(valor == 3):
            usuario = Usuario(int(input("Ingrese el ID del usuario a modificar: ")), input("Ingrese el nuevo username: "), input("Ingrese la nueva password: ") )
            UsuarioDao().update(usuario)

        if(valor == 4):
            usuario = Usuario(id_usuario=int(input("Ingrese el ID del usuario a eliminar: ")))
            UsuarioDao().delete(usuario)

    except Exception as e:
        log.error(f"Ocurrio un error: {e}")

else:
    print("Hasta la proxima crack :)")

