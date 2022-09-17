#Programa: Acceso_Datos.py
#Proposito: Ejecutar comando básicos en una DB MySQL.
#Autor: Ezequiel Lopez
#Fecha: 12/09/2022

from conexion import *
from persona import *
from logger import log

class Persona_Dao():
    '''
    DAO (Data Access Object)
    '''

    __seleccion = """SELECT * FROM persona"""
    __insert = """INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)"""
    __update = """UPDATE persona SET nombre= %s, apellido= %s, email=%s WHERE idpersona = %s"""
    __delete = """DELETE FROM persona WHERE idpersona = %s"""

    @classmethod
    def seleccionar(cls):
        cursor = Conexion().obtenerCursor()
        cursor.execute(cls.__seleccion)
        registros = cursor.fetchall()
        personas = []

        for registro in registros:
            persona = Persona(registro[0], registro[1], registro[2], registro[3])
            personas.append(persona)

        cursor.close()
        return personas      
         
    @classmethod
    def insert(cls, persona):
        cursor = Conexion().obtenerCursor()
        conexion = Conexion().obtenerConexion()
        
        valores = (persona.name, persona.lastname, persona.email)
        cursor.execute(cls.__insert, valores)
        conexion.commit()
        log.debug(f"Persona a insertar: \t{persona}")
        return cursor.rowcount
        


    @classmethod
    def update(cls, persona):
        cursor = Conexion().obtenerCursor()
        conexion = Conexion().obtenerConexion()

        valor = (
            persona.name,
            persona.lastname,
            persona.email,
            persona.id
        )
        
        cursor.execute(cls.__update, valor)
        conexion.commit()
        log.debug(f"Persona actualizada: {persona}\n")
        return cursor.rowcount

    @classmethod
    def delete(cls):
        cursor = Conexion().obtenerCursor()
        conexion = Conexion().obtenerConexion()

        valor = (int(input("Ingrese el ID de la persona a eliminar: ")),)
        
        cursor.execute(cls.__delete, valor)
        conexion.commit()
        return cursor.rowcount


if __name__ == "__main__":
    
    # Insertamos personas
    persona = Persona(Nombre=input("Nombre del usuario: "), Apellido=input("Apellido del usuario: "), Email=input("Email del usuario: "))
    regi = Persona_Dao().insert(persona)
    log.debug(f"Personas insertadas: {regi}\n")
    
    # Actualización de personas
    persona1 = Persona(104, Nombre="Tartini", Apellido="Claudio", Email="tartidio@yahoo.com")
    personas_actualizados = Persona_Dao().update(persona1)
    log.debug(f"Personas actualizadas: {personas_actualizados}")

    #Eliminación de personas
    personas_eliminadas = Persona_Dao().delete()
    log.debug(f"Personas eliminadas: {personas_eliminadas}")
    
    # Seleccionamos a las personas
    personas = Persona_Dao().seleccionar()
    for persona in personas:
        log.debug(persona)

    
