from usuarios import *
from conexion import *
from cursor_pool import *

class UsuarioDao():

    __seleccionar = """SELECT * FROM usuario"""
    __insert = """INSERT INTO usuario(id_usuario, username, password) VALUES (%s, %s, %s)"""
    __update = """UPDATE usuario SET username = %s, password = %s WHERE id_usuario = %s"""
    __delete = """DELETE FROM usuario WHERE id_usuario = %s"""

    @classmethod
    def seleccionar(cls):
        with CursorPool() as cursor:
            cursor.execute(cls.__seleccionar)
            registros = cursor.fetchall()
            personas = []
            
            for registro in registros:
                personas.append(Usuario(registro[0], registro[1], registro[2]))
            return personas

    @classmethod
    def insert(cls, usuario):
        with CursorPool() as cursor:
            cursor.execute(cls.__insert, (usuario.id, usuario.username, usuario.password))
            log.info(f"Usuario insertado: {cursor.rowcount}")

    @classmethod
    def update(cls, usuario):
        with CursorPool() as cursor:
            cursor.execute(cls.__update, (usuario.username, usuario.password, usuario.id))
            log.info(f"Usuarios actualizados: {cursor.rowcount}")

    @classmethod
    def delete(cls, usuario):
        with CursorPool() as cursor:
            cursor.execute(cls.__delete, (usuario.id, ))
            log.info(f"Usuario eliminados: {cursor.rowcount}")

if __name__ == "__main__":
    pass    
    #Select
    #personas = UsuarioDao().seleccionar()
    #for persona in personas:
    #    print(persona)
    
    #Insert
    #usuario = Usuario(16, "Florencia", "Flores")
    #print(usuario)
    #UsuarioDao().insert(usuario)

    #Update
    #usuario = Usuario(int(input("Ingrese el ID del usuario a modificar: ")), input("Ingrese el nuevo username: "), input("Ingrese la nueva password: ") )
    #print(usuario)
    #UsuarioDao().update(usuario)

    #Delete
    #usuario = Usuario(4)
    #print(usuario)
    #UsuarioDao().delete(usuario)




