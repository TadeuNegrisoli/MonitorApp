DEFAULT_INTERVALO = 5    #segundos entre verificações (fallback por site)
DEFAULT_TIMEOUT   = 10   #segundos aguardando resposta HTTP (fallback por site)
RETRY_ATTEMPTS    = 2    #tentativas antes de marcar offline
RETRY_DELAY       = 5    #segundos entre tentativas

UI_REFRESH_MS  = 1000   #intervalo do loop_refresh (milissegundos)
WORKER_SLEEP_S = 1      #intervalo do worker loop (segundos)

DB_PATH  = "sites_cadastrados.json"
LOG_PATH = "erros.log"