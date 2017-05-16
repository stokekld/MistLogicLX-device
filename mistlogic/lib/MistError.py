import logging, os

MAIN_DIR = os.environ["MAIN_DIR"]

# Archivo y configuracion del log
logPath = os.path.join(MAIN_DIR, 'mist.log')
logging.basicConfig(filename=logPath,level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')

class Error(Exception):
    """
    Clase para excepciones
    """
    message = ''

    def __init__(self, msg):
        self.message = msg
        self.warn()

    def warn(self):
        logging.warning(self.message)

class Info():
    """
    Clase para mensajes nivel info
    """
    message = ''

    def __init__(self, msg):
        self.message = msg
        self.info()

    def info(self):
        logging.info(self.message)

