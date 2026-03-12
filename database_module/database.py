import json, os

DB_PATH= "sites_cadastrados.json"

def carregar_sites():
    if not os.path.exists(DB_PATH): return []
    with open(DB_PATH, "r", encoding="utf-8") as f:
        try: return json.load(f)
        except json.JSONDecodeError: return []

def adicionar_site_db(url, intervalo):
    try: intervalo= int(intervalo)
    except ValueError: intervalo= 5 
    
    sites= carregar_sites()
    if any(s["url"] == url for s in sites): return
    
    sites.append({"url": url, "intervalo": intervalo, "status": "Conectando"})
    with open(DB_PATH, "w", encoding="utf-8") as f: json.dump(sites, f, indent=4)

def remover_site_db(url):
    sites= [s for s in carregar_sites() if s["url"] != url]
    with open(DB_PATH, "w", encoding="utf-8") as f: json.dump(sites, f, indent=4)

def up_status(url, status):
    sites= carregar_sites()
    for s in sites:
        if s["url"] == url: s["status"]= status
    with open(DB_PATH, "w", encoding="utf-8") as f: json.dump(sites, f, indent=4)