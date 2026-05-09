import json, os, threading, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from monitor_module.status import Status
from core.config import DB_PATH, DEFAULT_INTERVALO, DEFAULT_TIMEOUT
_db_lock= threading.RLock()

def carregar_sites():
    with _db_lock:
        if not os.path.exists(DB_PATH): return []
        with open(DB_PATH, "r", encoding="utf-8") as f:
            try: return json.load(f)
            except json.JSONDecodeError: return []

def adicionar_site_db(url, intervalo, timeout=DEFAULT_TIMEOUT):
    try: intervalo= int(intervalo)
    except ValueError: intervalo= DEFAULT_INTERVALO
    try: timeout= int(timeout)
    except ValueError: timeout= DEFAULT_TIMEOUT
    with _db_lock:
        sites= carregar_sites()
        if any(s["url"] == url for s in sites): return
        sites.append({"url": url, "intervalo": intervalo, "timeout": timeout, "status": Status.CONECTANDO})
        with open(DB_PATH, "w", encoding="utf-8") as f: json.dump(sites, f, indent=4)

def remover_site_db(url):
    with _db_lock:
        sites= [s for s in carregar_sites() if s["url"] != url]
        with open(DB_PATH, "w", encoding="utf-8") as f: json.dump(sites, f, indent=4)

def up_status(url, status):
    with _db_lock:
        sites= carregar_sites()
        for s in sites:
            if s["url"] == url: s["status"]= status
        with open(DB_PATH, "w", encoding="utf-8") as f: json.dump(sites, f, indent=4)