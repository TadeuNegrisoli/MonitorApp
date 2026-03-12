import os
from datetime import datetime

def get_logs():
    if not os.path.exists("erros.log"): return "Sem registros."
    with open("erros.log", "r", encoding="utf-8") as f: return f.read()

def gerar_novo_log():
    if os.path.exists("erros.log"):
        data_hora= datetime.now().strftime("%d-%m-%Y_%H-%M")
        os.rename("erros.log", f"erros_bckp_{data_hora}.log")
    
    with open("erros.log", "w", encoding="utf-8") as f: pass