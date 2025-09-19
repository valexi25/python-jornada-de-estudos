from conexion import Conexion
from persona import Persona
from logger_base import log
from cursos_del_pool import CursorDelPool
class PersonaDAO():
    
    _SELECIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona (nombre, apellido, email) VALUES(%s,%s,%s)'
    _ATUALIZAR = 'UPDATE persona SET nombre= %s, apellido=%s,email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def selecionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0],registro[1],registro[2],registro[3])
                personas.append(persona)
            return personas
    
    @classmethod
    def insertar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre,persona.apellido,persona.email)
            cursor.execute(cls._INSERTAR,valores)
            log.debug(f'Personas a insertada: {persona}')
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._ATUALIZAR,valores)
            log.debug(f'Persona atualizada: {persona}')
            return cursor.rowcount
    
    @classmethod
    def eliminar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.id_persona,)
            cursor.execute(cls._ELIMINAR,valores)
            log.debug(f'Objeto eliminado: {persona}')
            return cursor.rowcount
            
if __name__ == '__main__':
    #insetar un registro
    #persona1 = Persona(nombre='Alejandra',apellido='Tellez',email='atellez@gmail.com')
    #personas_insertadas = PersonaDAO.insertar(persona1)
    #log.debug(f'Personas insertados: {personas_insertadas}')

    #Atualizar un registro
    persona1 = Persona(nombre='Juan',apellido='Perez',email='jperes@mail.com',id_persona=1)
    personas_atualizados = PersonaDAO.actualizar(persona1)
    log.debug(f'Personas atualizadas: {personas_atualizados}')

    #eliminar registro
    persona1 =Persona(id_persona=20)
    personas_elimindar = PersonaDAO.eliminar(persona1)
    log.debug(f'Personas eliminadas: {personas_elimindar}')

    #selecionar objetos
    personas = PersonaDAO.selecionar()
    for persona in personas:
        log.debug(persona)