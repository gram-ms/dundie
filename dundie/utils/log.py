import logging
from logging import handlers

log = logging.getLogger("dundie")
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s "
    "l:%(lineno)d f:%(filename)s: %(message)s"
)


def get_logger(logfile="dundie.log"):
    """Returns a configured logger"""
    # FileHandler
    # Instance
    fh = handlers.RotatingFileHandler(
        logfile,
        maxBytes=10**6,  # Recomendado 10**6 1MB
        backupCount=1,  # N de uns de arquivos logs
    )
    # formataçào
    fh.setFormatter(fmt)
    # nível
    fh.setLevel("WARNING")
    # destino
    log.addHandler(fh)
    return log
