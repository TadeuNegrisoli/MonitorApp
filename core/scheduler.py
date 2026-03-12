import sys, os, time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from monitor_module.monitor import verificar_status_site, salvar_log_erro, alertar_windows
from database_module.database import carregar_sites, up_status

ultimo_check= {}
def varredura_completa():
    agora= time.time()
    sites_antes= {s['url']: s.get('status') for s in carregar_sites()}
    
    for site in carregar_sites():
        url= site["url"]
        intervalo= site.get("intervalo", 5)
        if url not in ultimo_check or (agora - ultimo_check[url]) >= intervalo:
            res= verificar_status_site(url)
            status_antigo= sites_antes.get(url)
            up_status(url, res["status"])
            if res["status"] != "Online": salvar_log_erro(res)
            if status_antigo in ["Online", "Conectando"] and res["status"] != "Online":
                alertar_windows(url, res["erro"])
                
            ultimo_check[url]= agora