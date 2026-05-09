from enum import Enum

class Status(str, Enum):
    ONLINE      = "Online"
    OFFLINE     = "Offline"
    CONECTANDO  = "Conectando"
    ERRO_STATUS = "Erro de Status"