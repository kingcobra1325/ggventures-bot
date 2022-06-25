import os, logging
import __main__

try:
    from dotenv import load_dotenv
except Exception as e:
    os.system(f"pip install python-dotenv")
    from dotenv import load_dotenv

load_dotenv('.env')

def logger_level():
    level = os.environ['LOGGER_LEVEL']
    if level == 'DEBUG':
        return logging.DEBUG
    elif level == 'INFO':
        return logging.INFO
    elif level == 'WARNING':
        return logging.WARNING
    elif level == 'ERROR':
        return logging.ERROR
    elif level == 'CRITICAL':
        return logging.CRITICAL
    else:
        raise Exception("Invalid Logger Level value...")

def initialize_logger(name=''):
    if name == '__main__':
        CWD = os.path.dirname(os.path.realpath(__main__.__file__))
        string_format = "|%(asctime)s|{%(module)s}-(%(funcName)s) %(lineno)d-[%(levelname)s] %(message)s"
        FORMAT = logging.Formatter(string_format)
        log_file_path = os.path.join(CWD, f"GGVentures_LOG.log")
        logger = logging.getLogger('__main__')
        logger.setLevel(logger_level())
        # Add Log File
        file_handler = logging.FileHandler(filename=log_file_path, mode="w", encoding="UTF-8")
        file_handler.setFormatter(FORMAT)
        logger.addHandler(file_handler)
        # Add Console Logo Display
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(FORMAT)
        logger.addHandler(console_handler)

    else:
        logger = logging.getLogger('__main__')
    
    return logger
        

class LoggerMixin:

    logger = initialize_logger()