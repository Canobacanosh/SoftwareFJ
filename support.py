import logging
import os
import traceback

#POR AQUI CREAMOS LAS EXCEPCIONES PERSONALIZADAS

#Clase que hereda
class ErrorSoftwareFJ(Exception):
    [span_3](start_span)[span_4](start_span)
    def _init_(self, mensaje):
        super()._init_(mensaje)

        Vigilante.add_to_log("error", mensaje)

#Clases herederas
class ErrorDatoInvalido(ErrorSoftwareFJ):
  [span_5](start_span)
  pass

class ErrorOperacionInvalida(ErrorSoftwareFJ):
  [span_6](start_span)
  pass

class ErrorCalculoInconsistente(ErrosSoftwareFJ):
  [span_7](start_span)[span_8](start_span)
  pass


#CLASE "VIGILANTE", usamos la alegoría del vigilante porque es la encargada de hacer las veces de vigilante, anotar en la bitácora
#hora, nivel, tipo y mensajae
class Vigilante():
  @staticmethod
  def __set_logger(self):
    log_directory ="logs"
    log_filename = "support.log"

    #Crear el directorio si no existe
    if not os.path.exists(log_directory):
      os.makedirs(log_directory)

    logger = logging.getLogger("SoftwareFJ")
    if not logger.handlers:
      logger.setLevel(logging.DEBUG)

    log_path = os.path.join(log_directory, log_filename)
    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    #file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', "%Y-%m-%d %H:%M:%S")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger

@classmethod
def add_to_log(cls,level,message):
  try:
    logger = cls.__set_logger()

    metodos = {
        "critical": logger.critical,
        "debug": logger.debug,
        "error": logger.error,
        "info": logger.info,
        "warn": logger.warn
    }

    metodos.get(level.lower()), logger.info(message)

  except Exception as ex:
    print(f"Error en el log: {ex}")
    print(traceback.format_exc())

#    if (level == "critical"):
#      logger.critical(message)
#    elif (level == "debug"):
#      logger.debug(message)
#    elif (level == "error"):
#      logger.error(message)
#    elif (level == "info"):
#      logger.info(message)
#    elif (level == "warn"):
#      logger.warn(message)
#  except Exception as ex:
#    print(traceback.format_exc())
#    print(ex)
