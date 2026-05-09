import sys, os, time
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from monitor_module.monitor import verificar_status_site, salvar_log_erro, alertar_windows
from database_module.database import carregar_sites, up_status
from monitor_module.status import Status
from core.config import RETRY_ATTEMPTS, RETRY_DELAY, DEFAULT_INTERVALO, DEFAULT_TIMEOUT

ultimo_check= {}
def varredura_completa():
    agora= time.time()
    sites= carregar_sites()
    sites_antes= {s['url']: s.get('status') for s in sites}
    for url_removida in [u for u in ultimo_check if u not in sites_antes]:
        del ultimo_check[url_removida]

    for site in sites:
        url= site["url"]
        intervalo= site.get("intervalo", DEFAULT_INTERVALO)
        timeout= site.get("timeout", DEFAULT_TIMEOUT)
        if url not in ultimo_check or (agora - ultimo_check[url]) >= intervalo:
            res= verificar_status_site(url, timeout=timeout)
            for _ in range(RETRY_ATTEMPTS):
                if res["status"] == Status.ONLINE: break
                time.sleep(RETRY_DELAY)
                res= verificar_status_site(url, timeout=timeout)

            status_antigo= sites_antes.get(url)
            up_status(url, res["status"])
            if res["status"] != Status.ONLINE: salvar_log_erro(res)
            if status_antigo in [Status.ONLINE, Status.CONECTANDO] and res["status"] != Status.ONLINE:
                alertar_windows(url, res["erro"])

            ultimo_check[url]= agora