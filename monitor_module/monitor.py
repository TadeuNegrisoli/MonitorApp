import requests, time, urllib3
from datetime import datetime
from winotify import Notification, audio

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def alertar_windows(site, erro):
    toast= Notification(app_id="MonitorApp", title="Site Off!", msg=f"Erro: {erro}", duration="short")
    toast.set_audio(audio.Default, loop=False)
    toast.show()

def verificar_status_site(url, timeout=10):
    res= {
        "url": url, "status": "Offline", "code": None, "tempo_resp": 0,
        "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "erro": None
    }
    try:
        inicio= time.time()
        headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response= requests.get(url, timeout=timeout, headers=headers, verify=False)
        res["code"]= response.status_code
        res["tempo_resp"]= round(time.time() - inicio, 2)
        if 200 <= response.status_code < 400:
            res["status"]= "Online"
        else:
            res["status"]= "Erro de Status"; res["erro"]= f"HTTP {response.status_code}"
    except Exception as e: res["erro"]= str(e)
    return res

def salvar_log_erro(res):
    if res["status"] != "Online":
        with open("erros.log", "a", encoding="utf-8") as f:
            f.write(f"[{res['timestamp']}] SITE: {res['url']} | ERRO: {res['erro']} | CODE: {res['code']}\n\n")