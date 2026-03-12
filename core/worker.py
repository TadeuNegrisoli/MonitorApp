import threading, time
from .scheduler import varredura_completa

def run_loop():
    while True:
        varredura_completa()
        time.sleep(1)

def start_worker():
    threading.Thread(target=run_loop, daemon=True).start()