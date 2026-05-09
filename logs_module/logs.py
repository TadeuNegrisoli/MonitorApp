import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from datetime import datetime
from core.config import LOG_PATH

def get_logs():
    if not os.path.exists(LOG_PATH): return "Sem registros."
    with open(LOG_PATH, "r", encoding="utf-8") as f: return f.read()

def gerar_novo_log():
    if os.path.exists(LOG_PATH):
        data_hora= datetime.now().strftime("%d-%m-%Y_%H-%M")
        os.rename(LOG_PATH, f"erros_bckp_{data_hora}.log")
    
    with open(LOG_PATH, "w", encoding="utf-8") as f: pass