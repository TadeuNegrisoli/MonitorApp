import threading, time, traceback
from .scheduler import varredura_completa
from .config import WORKER_SLEEP_S, LOG_PATH

def run_loop():
    while True:
        try:
            varredura_completa()
        except Exception:
            with open(LOG_PATH, "a", encoding="utf-8") as f:
                f.write(f"[WORKER ERRO]\n{traceback.format_exc()}\n")
        time.sleep(WORKER_SLEEP_S)

def start_worker():
    threading.Thread(target=run_loop, daemon=True).start()