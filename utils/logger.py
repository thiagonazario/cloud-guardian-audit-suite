import logging
import sys

def setup_custom_logger(name):
    # Formatação: Data - Nome - Nível - Mensagem
    formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Handler para exibir no terminal (stdout)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    return logger

# Instância padrão para ser importada pelos outros scripts
logger = setup_custom_logger('CloudGuardian')