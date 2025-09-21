from cursos_del_pool import CursorDelPool
from logger_base import log
from usuario import Usuario
class UsuarioDAO:

    _SELECT = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username,password) VALUES(%s,%s)'
    _ATUALIZAR = 'UPDATE usuario SET username=%s, password= %s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def selecionar(cls):
        with CursorDelPool() as cursor:
            log.debug('Selecionando usuarios')
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0],registro[1],registro[2])
                usuarios.append(usuario)
            return usuarios
        
    @classmethod
    def insertar(cls,usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a insertar: {usuario}')
            valores = (usuario.username,usuario.password)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls,usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a actualizar {usuario}')
            valores = (usuario.username,usuario.password,usuario.id_usuario)
            cursor.execute(cls._ATUALIZAR,valores)
            return cursor.rowcount
        
    @classmethod
    def eliminar(cls,usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a eliminar: {usuario}')
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount

if __name__ == '__main__':
    #usuaio1 = Usuario(username='vaneza',password=123)
    #usuario_insertado = UsuarioDAO.insertar(usuaio1)
    #log.debug(f'Usuario insertado {usuario_insertado}')

    #modificar
    #usuario1 = Usuario(username='alex',password=123,id_usuario=3)
    #usuario_modificado = UsuarioDAO.actualizar(usuario1)
    #log.debug(f'Usuario Monidicado {usuario1}')

    #eliminar un registro
    #usuario1 = Usuario(id_usuario=4)
    #eliminada = UsuarioDAO.eliminar(usuario1)
    #log.debug(f'Usuario Eliminado {eliminada}')

    #selecionar
    usuarios = UsuarioDAO.selecionar()
    for usuario in usuarios:
        log.debug(usuario) 