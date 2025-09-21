import logging as log
log.basicConfig(level=log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s: %(lineno)s] %(message)s',
                datefmt ='%I:%M:%S %p',
                handlers=[
                        log.FileHandler('capa_datos.log'),
                        log.StreamHandler()
                ])

if __name__ == '__main__':
    log.debug('Mensaje a nivel de bug')
    log.info('Menage nivel de info')
    log.warning('mensaje a nivel de warning')
    log.error('Mensage a nivel de erro')
    log.critical('Mensage a nivel de critical')

