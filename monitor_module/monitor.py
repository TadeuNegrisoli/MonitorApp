import requests, time, urllib3, threading, sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from monitor_module.status import Status
from core.config import DEFAULT_TIMEOUT, LOG_PATH
from datetime import datetime
from winotify import Notification, audio

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
_log_lock= threading.Lock()

def alertar_windows(site, erro):
    toast= Notification(app_id="MonitorApp", title="Site Off!", msg=f"Erro: {erro}", duration="short")
    toast.set_audio(audio.Default, loop=False)
    toast.show()

def verificar_status_site(url, timeout=DEFAULT_TIMEOUT):
    res= {
        "url": url, "status": Status.OFFLINE, "code": None, "tempo_resp": 0,
        "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "erro": None
    }
    try:
        inicio= time.time()
        headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response= requests.get(url, timeout=timeout, headers=headers, verify=False)
        res["code"]= response.status_code
        res["tempo_resp"]= round(time.time() - inicio, 2)
        if 200 <= response.status_code < 400:
            res["status"]= Status.ONLINE
        else:
            res["status"]= Status.ERRO_STATUS; res["erro"]= f"HTTP {response.status_code}"
    except requests.exceptions.Timeout:
        res["erro"]= f"Timeout após {timeout}s"
    except requests.exceptions.ConnectionError as e:
        msg= str(e).lower()
        if "getaddrinfo" in msg or "name or service" in msg:
            res["erro"]= "DNS não encontrado!"
        elif "connection refused" in msg or "actively refused" in msg:
            res["erro"]= "Conexão recusada!"
        else:
            res["erro"]= "Erro de conexão!"
    except requests.exceptions.RequestException as e:
        res["erro"]= f"Erro de rede: {str(e)}"
    return res

def salvar_log_erro(res):
    if res["status"] != Status.ONLINE:
        with _log_lock:
            with open(LOG_PATH, "a", encoding="utf-8") as f:
                f.write(f"[{res['timestamp']}] SITE: {res['url']} | ERRO: {res['erro']} | CODE: {res['code']}\n\n")